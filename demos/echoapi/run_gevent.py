#!/usr/bin/env python
#!-*- coding=utf-8 -*-

from gevent.wsgi import WSGIServer
from gevent import monkey
import config

monkey.patch_all()

if '__main__' == __name__:
    from run import app
    server = WSGIServer((config.SVR_CONFIG['host'], config.SVR_CONFIG['port']), app)
    server.serve_forever()

