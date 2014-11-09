#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import inspect
import json
import functools
import os.path as osp
from mako.lookup import TemplateLookup
from mako.template import Template
from flask import url_for, request, Blueprint
from ...proto.fields import BasicField

__all__ = [
    'ApiException', 'webapi', 'webapi_class', 'install_api_list',
]

_api_list = []

class ApiException(Exception):
    def __init__(self, result = -1, message = 'Unknown error'):
        self._result = result
        self._message = message

    @property
    def result(self):
        return self._result

    @property
    def message(self):
        return self._message

class _ApiMethodWrapper(object):
    def __init__(self, req_cls, rsp_cls, callback, exception_handler = None):
        self._req_cls = req_cls
        self._rsp_cls = rsp_cls
        self._callback = callback
        self._exception_handler = exception_handler
        method_name = callback.func_name
        if method_name.endswith('_POST'):
            self._dataset = 'form'
            self._http_method = ['POST',]
            self._method_name = method_name[:-5]
        elif method_name.endswith('_GET'):
            self._dataset = 'args'
            self._http_method = ['GET',]
            self._method_name = method_name[:-4]
        else:
            self._dataset = 'values'
            self._http_method = ['GET', 'POST',]
            self._method_name = method_name

    @property
    def request_type(self):
        return self._req_cls

    @property
    def response_type(self):
        return self._rsp_cls

    @property
    def http_method(self):
        return self._http_method

    @property
    def method_name(self):
        return self._method_name

    def __call__(self, obj):
        if self._req_cls is not None:
            req = self._req_cls()
            reqdata = getattr(request, self._dataset)
            for key, field_info in self._req_cls._get_fields():
                if key not in reqdata:
                    if field_info.required:
                        logging.error('while calling %s, required field %s is missing',
                                    request.path, key)
                        return ''
                    continue
                if field_info.repeated:
                    setattr(req, key, reqdata.getlist(key))
                else:
                    setattr(req, key, reqdata.get(key))
        else:
            req = None
        rsp = self._rsp_cls()
        try:
            ret = self._callback(obj, req, rsp)
        except ApiException, ex:
            if self._exception_handler:
                self._exception_handler(req, rsp, ex)
        return rsp.to_json()     

def webapi(req_cls, rsp_cls, exception_handler = None):
    def _inner(callback):
        inner = _ApiMethodWrapper(req_cls, rsp_cls, callback, exception_handler)
        return functools.update_wrapper(inner, callback)
    return _inner

def webapi_class(app, **kwargs):
    def _inner(cls):
        global _api_list
        apis = inspect.getmembers(cls, lambda f: isinstance(f, _ApiMethodWrapper))
        for name, wrapper in apis:
            _api_list.append((app, cls, name, wrapper))
        return cls
    return _inner

def install_api_list(app, prefix):
    if not prefix.endswith('/'):
        prefix += '/'

    tpl_dir = osp.join(osp.dirname(osp.abspath(__file__)), 'templates')
    tpl_lookup = TemplateLookup(
        directories = [tpl_dir,],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
    )

    def _load_tpl(filename):
        return tpl_lookup.get_template(filename)

    @app.route(prefix)
    def api_list():
        tpl = _load_tpl('api_list.html')
        return tpl.render(url_prefix = prefix, api_list = _api_list)

    @app.route(prefix + '<int:index>')
    def api_detail(index):
        tpl = _load_tpl('api_detail.html')
        app, cls, method_name, wrapper = _api_list[index]
        url_route = app.name + '.' + cls.__name__ \
                if isinstance(app, Blueprint) else cls.__name__
        return tpl.render(
            url_prefix = prefix,
            api_url = url_for(url_route, name = wrapper.method_name),
            app = app,
            cls = cls,
            method_name = wrapper.method_name,
            wrapper = wrapper
        )


