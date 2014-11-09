#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import re
import inspect
from flask import abort, request, url_for, redirect, flash
from flask.views import View

class DispatchView(View):
    methods = ['GET', 'POST',]

    def __init__(self, *args, **kwargs):
        super(DispatchView, self).__init__(*args, **kwargs)

    def dispatch_request(self, name):
        name = name.lower()
        if '_' == name[0]:
            abort(404)
        method = None
        name_with_method = name + '_' + request.method.upper()
        if hasattr(self, name_with_method):
            method = getattr(self, name_with_method)
        elif hasattr(self, name):
            method = getattr(self, name)
        else:
            abort(404)
        if inspect.ismethod(method):
            return method()
        else:
            return method(self)

    def _redirect(self, entry, success = None, error = None):
        if error is not None:
            flash(error, 'danger')
        if success is not None:
            flash(success, 'success')
        return redirect(url_for('.' + self.__class__.__name__, name = entry))

    @classmethod
    def url_name(cls):
        name_parts = [x.lower() for x in re.findall('[A-Z]?[a-z0-9]*', cls.__name__) if x]
        name = '_'.join(name_parts)
        return name

    @classmethod
    def install_to(cls, app, decorators = []):
        name = cls.url_name()
        view_func = cls.as_view(cls.__name__)
        for decorator in decorators:
            view_func = decorator(view_func)
        app.add_url_rule('/%s/<name>/' % name, view_func = view_func)

def install_to(app, decorators = []):
    def _inner(cls):
        cls.install_to(app, decorators)
        return cls
    return _inner

