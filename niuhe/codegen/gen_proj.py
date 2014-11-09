#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import sys
import os
import os.path as osp
import json
import random
import logging
reload(sys)
sys.setdefaultencoding('u8')
from mako.template import Template
from mako.lookup import TemplateLookup

template_lookup = TemplateLookup(
    directories = [osp.join(osp.dirname(osp.abspath(__file__)), 'gen_proj_tpls'),],
    input_encoding  = 'utf-8',
    output_encoding = 'utf-8',
)

def mkdir_p(*paths):
    fullpath = osp.join(*paths)
    if not osp.isdir(fullpath):
        os.mkdir(fullpath)
    
def create_file_by_template(target_path, template_path, force_rewrite = True, **kwargs):
    if isinstance(target_path, list):
        target_path = osp.join(*target_path)
    if isinstance(template_path, list):
        template_path = osp.join(*template_path)
    if not force_rewrite and osp.exists(target_path):
        logging.info('目标%s已存在，跳过生成', target_path)
        return
    template = template_lookup.get_template(template_path)
    with file(target_path, 'w') as target_file:
        target_file.write(template.render(**kwargs))
    logging.info('生成%s完成', target_path)

def gen_proj_root(proj_name, modules):
    logging.info('正在生成项目根目录...')
    mkdir_p(proj_name)
    mkdir_p(proj_name, 'lib')
    mkdir_p(proj_name, 'doc')

    create_file_by_template(
        target_path     = [proj_name, 'run.py',],
        template_path   = 'run.py.tpl',
    )
    create_file_by_template(
        target_path     = [proj_name, 'run_gevent.py',],
        template_path   = 'run_gevent.py.tpl',
    )
    create_file_by_template(
        target_path     = [proj_name, 'devrun.sh',],
        template_path   = 'devrun.sh.tpl',
    )
    create_file_by_template(
        target_path     = [proj_name, 'config.py',],
        template_path   = 'config.py.tpl',
        secret_key      = ''.join([random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*(((()_+-=') for _ in xrange(32)])
    )

def gen_sub_dir(proj_name, mod, dirname, surfix):
    mkdir_p(proj_name, 'app', mod, dirname)
    create_file_by_template(
        target_path     = [proj_name, 'app', mod, dirname, '__init__.py',],
        template_path   = ['app', 'mod', dirname, '__init__.py.tpl'],
        force_rewrite   = False,
    )
    create_file_by_template(
        target_path     = [proj_name, 'app', mod, dirname, 'sample_%s.py' % surfix,],
        template_path   = ['app', 'mod', dirname, 'sample_%s.py.tpl' % surfix],
        force_rewrite   = False,
    )

def gen_module(proj_name, mod):
    logging.info('正在生成模块%s...', mod)

    mkdir_p(proj_name, 'app', mod)
    mkdir_p(proj_name, 'app', mod, 'templates')

    create_file_by_template(
        target_path     = [proj_name, 'app', mod, '__init__.py',],
        template_path   = ['app', 'mod', '__init__.py.tpl'],
        mod             = mod,
        proj            = proj_name,
    )

    gen_sub_dir(proj_name, mod, 'views', 'view')
    gen_sub_dir(proj_name, mod, 'protos', 'proto')
    gen_sub_dir(proj_name, mod, 'services', 'service')
    gen_sub_dir(proj_name, mod, 'forms', 'form')
    gen_sub_dir(proj_name, mod, 'models', 'model')


def gen_app_with_modules(proj_name, modules):
    logging.info('带模块app...')

    create_file_by_template(
        target_path     = [proj_name, 'app', '__init__.py',],
        template_path   = ['app', '__init_with_modules__.py.tpl'],
        modules         = modules,
    )
    for mod in modules:
        gen_module(proj_name, mod)

    mkdir_p(proj_name, 'app', '_common')
    create_file_by_template(
        target_path     = [proj_name, 'app', '_common', '__init__.py',],
        template_path   = ['app', '_common', '__init__.py.tpl'],
    )
    create_file_by_template(
        target_path     = [proj_name, 'app', '_common', 'forms.py',],
        template_path   = ['app', '_common', 'forms.py.tpl'],
        force_rewrite   = False,
    )
    create_file_by_template(
        target_path     = [proj_name, 'app', '_common', 'services.py',],
        template_path   = ['app', '_common', 'services.py.tpl'],
        force_rewrite   = False,
    )
    create_file_by_template(
        target_path     = [proj_name, 'app', '_common', 'models.py',],
        template_path   = ['app', '_common', 'models.py.tpl'],
        force_rewrite   = False,
    )
    mkdir_p(proj_name, 'app', '_common', 'templates')

def gen_app(proj_name, modules):
    logging.info('正在生成app目录,模块个数%d', len(modules))
    mkdir_p(proj_name, 'app')
    return gen_app_with_modules(proj_name, modules)

logging.basicConfig(
    level   = logging.DEBUG,
    format  = '%(asctime)s|%(levelname)s|%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
)

proj_name = sys.argv[1]
modules = sys.argv[2:]

if not modules:
    logging.error('请指定至少一个模块')
    sys.exit(-1)

gen_proj_root(proj_name, modules)
gen_app(proj_name, modules)
