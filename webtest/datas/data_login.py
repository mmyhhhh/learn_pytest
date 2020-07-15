# -*- coding:utf-8 -*-
# @Time    : 2020/6/26 10:01
# @Author  : mmy
# @File    : data_login

correct_data=[{'phone':'18684720553','pwd':'python','expected':'python'}]

incorrect_data1=[{'phone':'18684720553','pwd':'','expected':'请输入密码'},
                 {'phone': '', 'pwd': 'python', 'expected': '请输入手机号'},
                 {'phone': '186847', 'pwd': 'python', 'expected': '请输入正确的手机号'}]

incorrect_data2 = [{'phone': '18810444950', 'pwd': 'python1', 'expected': '此账号没有经过授权，请联系管理员!'},
                   {'phone': '18684720553', 'pwd': 'python1', 'expected': '帐号或密码错误!'}]


