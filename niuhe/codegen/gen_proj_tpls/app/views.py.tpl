#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import logging
from flask import request
from . import app, render_template
from .forms import *
from .models import *
from .services import *
from niuhe.flask_ext.dispatch_view import DispatchView, install_to

'''
TODO: Add codes like this
@install_to(module)
class Test(DispatchView):
    def echo(self):
        return request.args.echo
'''        
