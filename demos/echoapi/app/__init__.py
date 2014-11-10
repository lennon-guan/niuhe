#!/usr/bin/env python
#!-*- coding=utf-8 -*-

from flask import Flask
from api import module as api_modules
import config

app = Flask(__name__)
if hasattr(config, 'SECRET_KEY'):
    app.secret_key = config.SECRET_KEY 

app.register_blueprint(api_modules, url_prefix = '/api')

if config.DEBUG:
    from niuhe.flask_ext.webapi import install_api_list
    install_api_list(app, '/apilist/')
