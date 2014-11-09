#!/usr/bin/env python
#!-*- coding=utf-8 -*-

from flask import Flask
% for mod in modules:
from ${mod} import module as ${mod}_modules
% endfor
import config

app = Flask(__name__)
if hasattr(config, 'SECRET_KEY'):
    app.secret_key = config.SECRET_KEY 

% for mod in modules:
app.register_blueprint(${mod}_modules, url_prefix = '/${mod}')
% endfor

% if 'api' in modules:
if config.DEBUG:
    from niuhe.flask_ext.webapi import install_api_list
    install_api_list(app, '/apilist/')
% endif
