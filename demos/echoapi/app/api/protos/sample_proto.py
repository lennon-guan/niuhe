#!/usr/bin/env python
#!-*- coding=utf-8 -*-

from niuhe.proto import *

class CommonRequest(Message):
    pass

class SessionalRequest(Message):
    session_id  = required.StringField(
                    tag     = 10001,    # for tlv packing. not used yet
                    desc    = 'session id'
				  )

class ResponseWrapper(Message):
    result      = required.IntegerField()
    message     = optional.StringField()

class SimpleEchoReq(Message):
    '''
    This is a simple request type, with only one field named content
    '''
    content     = required.StringField()

class NextEchoReq(SessionalRequest):
    '''
    This is a message inheriting SessionalRequest, that makes it contains a field session_id which is defined in SessionalRequest
    '''
    content_items = repeated.StringField()  # content_items is an array of string

@extend_message(ResponseWrapper, 'data')
class EchoRsp(Message):
    '''
    EchoRsp shows the usage of extend_message decorator
    While using extend_message, the new message will become a field of the wrapper class.
    In this example, the new class we will get is like this:

    class __ResponseWrapper_EchoRsp_data_(Message):
        content     = required.StringField()
    class EchoRsp(Message):
        result      = required.IntegerField()
        message     = optional.StringField()
        data        = optional.MessageField(cls = __ResponseWrapper_EchoRsp_data_)
    '''    
    content     = required.StringField()

