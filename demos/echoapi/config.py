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

SECRET_KEY = '$kinQ1ye93L!dVMC1V)L@u!$GkJer(v)'

logging.basicConfig(
    level   = logging.DEBUG if DEBUG else logging.INFO,
    format  = '%(asctime)s|%(levelname)s|%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
)

