#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import logging

DEBUG = True

TEMPLATE_CONFIG = dict(
	template_additional_paths = [
	],
)

SVR_CONFIG = dict(
    host    = '127.0.0.1',
    port    = 56789,
    debug   = DEBUG,
)

SECRET_KEY = '${secret_key}'

logging.basicConfig(
    level   = logging.DEBUG if DEBUG else logging.INFO,
    format  = '%(asctime)s|%(levelname)s|%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
)

