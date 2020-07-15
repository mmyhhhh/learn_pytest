# -*- coding:utf-8 -*-
# @Time    : 2020/6/26 10:17
# @Author  : mmy
# @File    : testlogin

import unittest
from webtest.pages.loginpage import LoginPage
from webtest.pages.indexpage import IndexPage
from selenium import webdriver
from webtest.datas import data_login
from ddt import ddt, data
import time


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = 'http://120.78.128.25:8765/Index/login.html'
        cls.driver.get(url)
        cls.loginpage = LoginPage(cls.driver)
        cls.indexpage = IndexPage(cls.driver)

    def setUp(self):
        self.loginpage.ele_phone.clear()
        self.loginpage.ele_pwd.clear()
        # pass

    def tearDown(self):
        # self.loginpage.ele_phone.clear()
        # # 每次用例执行完之后清空输入框，当执行完登录成功的操作后，再执行清空操作会报错，所以将清空操作放在用例执行前，或者每条用例执行完使用refresh函数
        # self.loginpage.ele_pwd.clear()
        # self.driver.refresh()
        pass

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

    @data(*data_login.incorrect_data1)
    def test_login_1(self, data):
        # print(data)
        self.loginpage.submit_login(data['phone'], data['pwd'])
        text = self.loginpage.ele_error.text
        self.assertTrue(data['expected'], text)

    @data(*data_login.incorrect_data2)
    def test_login_2(self, data):
        # print(data)
        self.loginpage.submit_login(data['phone'], data['pwd'])
        text = self.loginpage.ele_popup.text
        self.assertTrue(data['expected'], text)

    @data(*data_login.correct_data)
    def test_login_3(self, data):
        # print(data)
        self.loginpage.submit_login(data['phone'], data['pwd'])
        text = self.indexpage.ele_user.text
        self.assertIn(data['expected'], text)
