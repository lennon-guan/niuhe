#!/usr/bin/env python
#!-*- coding=utf-8 -*-

'''
	Generate by gen_proj.py

   //////////////////////////////////////////////////////////////
   //                        _ooOoo_                           //
   //                       o8888888o                          //
   //                       88" . "88                          //
   //                       (| ^_^ |)                          //
   //                       O\  =  /O                          //
   //                    ____/`---'\____                       //
   //                  .'  \\|     |//  `.                     //
   //                 /  \\|||  :  |||//  \                    //
   //                /  _||||| -:- |||||-  \                   //
   //                |   | \\\  -  /// |   |                   //
   //                | \_|  ''\---/''  |   |                   //
   //                \  .-\__  `-`  ___/-. /                   //
   //              ___`. .'  /--.--\  `. . ___                 //
   //            ."" '<  `.___\_<|>_/___.'  >'"".              //
   //          | | :  `- \`.;`\ _ /`;.`/ - ` : | |             //
   //          \  \ `-.   \_ __\ /__ _/   .-` /  /             //
   //    ========`-.____`-.___\_____/___.-`____.-'========     //
   //                         `=---='                          //
   //    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    //
   //        佛祖保佑           永无BUG        永不修改           //
   //////////////////////////////////////////////////////////////

'''

import sys
reload(sys)
sys.setdefaultencoding('u8')

from app import app
import config

if '__main__' == __name__:
    app.run(**config.SVR_CONFIG)

