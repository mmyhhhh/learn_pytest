# -*- coding:utf-8 -*-
# @Time    : 2020/6/26 10:17
# @Author  : mmy
# @File    : testbid

import unittest
from webtest.pages.loginpage import LoginPage
from webtest.pages.indexpage import IndexPage
from selenium import webdriver
from webtest.datas import data_login
from ddt import ddt,data
import time
import pytest


def idfn(val):             #val 代表了parametrize参数化后的参数值，例如这里表示每一个用例数据词典，val可以换为其他字符串，idfn也可以使用其他的函数名
    # 将每个 val 都加 1
    return val['expected']  #取字典中的期望值作为子用例名称


class TestBid:

    # @pytest.mark.run(order=1)
    # @pytest.mark.demo
    @pytest.mark.usefixtures('init_driver')  #单独使用 usefixtures 不能使用 fixture 的返回值，若使用返回值需要将fixture函数作为参数放到测试函数中。
    @pytest.mark.parametrize("login",data_login.correct_data,ids=idfn,indirect=True)  #将idfn赋值给ids设置子用例名称
    def test_login_1(self,init_driver,login):  # 使用返回值需要将fixture函数init_driver作为参数放到测试函数中
        # print(data)
        # driver,loginpage,indexpage=init_driver # 使用fixture函数init_driver的返回值
        # loginpage.submit_login(data['phone'],data['pwd'])
        # text=loginpage.ele_error.text
        # assert(data['expected']==text)
        pass