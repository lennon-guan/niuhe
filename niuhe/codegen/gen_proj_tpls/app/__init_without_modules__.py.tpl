#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import os.path as osp
from flask import Flask, url_for, request, get_flashed_messages
from mako.lookup import TemplateLookup
import config

app = Flask(__name__)
if hasattr(config, 'SECRET_KEY'):
    app.secret_key = config.SECRET_KEY 

_app_template_folder = osp.join(
    osp.abspath(osp.dirname(__file__)),
    'templates',
)
    
_tpl_lookup = TemplateLookup(
    directories     = [ _app_template_folder ] + config.TEMPLATE_CONFIG['template_additional_paths'],
    module_directory= osp.join(config.TEMPLATE_CONFIG['template_module_path'], '${proj}'),
    input_encoding  = 'utf-8',
    output_encoding = 'utf-8',
)

def render_template(template_name, **kwargs):
    template = _tpl_lookup.get_template(template_name)
    params = dict(
        url_for = url_for,
        request = request,
        get_flashed_messages = get_flashed_messages
    )
    params.update(kwargs)
    return template.render(**params)

from .views import *
