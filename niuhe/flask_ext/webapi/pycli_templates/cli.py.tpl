#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import requests

class ${ApiName}(object):
    def __init__(self, target_root_url):
        self._target_root_url = target_root_url
        self._session = requests.Session()

    def get_data(self, api_url, **datas):
        return self._session.get(self._target_root_url + api_url, data = datas)

    def post_data(self, api_url, **datas):
        return self._session.post(self._target_root_url + api_url, data = datas)

% for app, cls, method_name, wrapper in api_list:
    def 
% endfor
