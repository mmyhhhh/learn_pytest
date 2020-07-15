# -*- coding:utf-8 -*-
# @Time    : 2020/6/26 20:40
# @Author  : mmy
# @File    : testloginpytest


import unittest
from webtest.pages.loginpage import LoginPage
from webtest.pages.indexpage import IndexPage
from selenium import webdriver
from webtest.datas import data_login
from ddt import ddt,data
import time
import pytest
import allure

@allure.step('获取测试期望结果作为测试用例名称')
def idfn(val):             #val 代表了parametrize参数化后的参数值，例如这里表示每一个用例数据词典，val可以换为其他字符串，idfn也可以使用其他的函数名
    # 将每个 val 都加 1
    return val['expected']  #取字典中的期望值作为子用例名称

@allure.feature('登录用例')
class TestLogin:

    @allure.story('账户、密码未输入用例')
    @pytest.mark.run(order=1)
    @pytest.mark.demo
    @pytest.mark.usefixtures('init_driver','setup')  #单独使用 usefixtures 不能使用 fixture 的返回值，若使用返回值需要将fixture函数作为参数放到测试函数中。
    @pytest.mark.parametrize("data",data_login.incorrect_data1,ids=idfn)  #将idfn赋值给ids设置子用例名称
    def test_login_1(self,data,init_driver):  # 使用返回值需要将fixture函数init_driver作为参数放到测试函数中
        # print(data)
        # with allure.attach('输入用户名、密码'):
        allure.attach('输入用户名、密码')
        driver,loginpage,indexpage=init_driver # 使用fixture函数init_driver的返回值
        loginpage.submit_login(data['phone'],data['pwd'])
        text=loginpage.ele_error.text
        assert(data['expected']==text)


    @allure.story('账户、密码输入错误用例')
    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures('init_driver','setup')
    @pytest.mark.parametrize('data', data_login.incorrect_data2)
    def test_login_2(self,data,init_driver):
        # print(data)
        # with allure.attach('输入用户名、密码'):
        #     allure.attach(data)
        driver, loginpage, indexpage = init_driver
        loginpage.submit_login(data['phone'],data['pwd'])
        text=loginpage.ele_popup.text
        assert(data['expected']==text)


    @allure.story('登录成功用例')
    @pytest.mark.last
    @pytest.mark.usefixtures('init_driver', 'setup')
    @pytest.mark.parametrize('data', data_login.correct_data)
    def test_login_3(self,data,init_driver,setup):
        # print(data)
        # with allure.attach('输入用户名、密码'):
        #     allure.attach(data)
        driver, loginpage, indexpage = init_driver
        loginpage.submit_login(data['phone'],data['pwd'])
        text=indexpage.ele_user.text
        assert(data['expected'] in text)