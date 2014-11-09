#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('u8')
from messages import *
from fields import *
import pprint

class LoginRequest(Message):
    username    = StringField(required = True)
    password    = StringField(required = True)

class CommonResponse(Message):
    result      = IntegerField(required = True)
    message     = StringField(required = False)

@extend_message(CommonResponse, 'data')
class LoginResponse(Message):
    token       = StringField(repeated = True)


rsp = LoginResponse()
rsp.result = -1
rsp.message = '样子问题'
print rsp.has_data

rsp.data = LoginResponse.data.new()
rsp.data.token.append('aaaaaaa')
rsp.data.token.append('bbbbbbb')
rsp_json = rsp.to_json(ensure_ascii = False, indent = 4)
print rsp.has_data
print rsp_json, rsp.data.token[0]

rsp2 = LoginResponse()
rsp2.from_json(rsp_json)
print rsp2.data.token[0]
