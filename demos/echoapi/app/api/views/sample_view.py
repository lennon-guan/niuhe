#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import logging
from flask import request
from niuhe.flask_ext.dispatch_view import DispatchView, install_to
from niuhe.flask_ext.webapi import *

from .. import module, render_template
from ..forms.sample_form import *
from ..models.sample_model import *
from ..services.sample_service import *
from ..protos.sample_proto import *


@install_to(module)
@webapi_class(module)
class SampleEcho(DispatchView):

    @webapi(SimpleEchoReq, EchoRsp)
    def simple_echo_GET(self, req, rsp):
        rsp.result = 0
        rsp.data = EchoRsp.data.new()
        rsp.data.content = req.content

    @webapi(NextEchoReq, EchoRsp)
    def next_echo(self, req, rsp):
        rsp.result = 10086
        rsp.message = 'test'
        rsp.data = EchoRsp.data.new()
        rsp.data.content = '#'.join(req.content_items)
