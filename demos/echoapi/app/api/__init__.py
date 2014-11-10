#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import os.path as osp
from flask import Blueprint, url_for, request, get_flashed_messages
from mako.lookup import TemplateLookup
import config

module = Blueprint('api', __name__)

_mod_template_folder = osp.join(
    osp.abspath(osp.dirname(__file__)),
    'templates',
)

_common_template_folder = osp.join(
    osp.abspath(osp.dirname(__file__)),
    '..',
    '_common',
    'templates',
)

_tpl_lookup = TemplateLookup(
    directories     = [ _mod_template_folder, _common_template_folder ],
    input_encoding  = 'utf-8',
    output_encoding = 'utf-8',
)

def render_template(template_name, **kwargs):
    template = _tpl_lookup.get_template(template_name)
    params = dict(
        url_for = url_for,
        request = request,
        get_flashed_messages = get_flashed_messages,
    )
    params.update(kwargs)
    return template.render(**params)

from .views import *

