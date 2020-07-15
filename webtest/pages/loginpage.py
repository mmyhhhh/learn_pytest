# -*- coding:utf-8 -*-
# @Time    : 2020/6/26 10:17
# @Author  : mmy
# @File    : loginpage

from webtest.common import contains
from webtest.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage(BasePage):
    phone_locator = (By.XPATH, "//input[@name='phone']")
    pwd_locator = (By.XPATH, "//input[@name='password']")
    error_locator=(By.XPATH,"//div[@class='form-error-info']")
    popup_locator=(By.XPATH,"//div[@class='layui-layer-content']")

    @property
    def ele_phone(self)-> WebElement:
        return self.get_element_visibility(self.phone_locator)

    @property
    def ele_pwd(self)-> WebElement:
        return self.get_element_visibility(self.pwd_locator)

    def submit_login(self,phone,pwd):
        self.ele_phone.send_keys(phone)
        self.ele_pwd.send_keys(pwd)
        return self.ele_pwd.submit()  # form表单的submit提交功能，form表单里任意一个元素定位后都可直接跟submit进行提交数据

    @property
    def ele_error(self)-> WebElement:
        return self.get_element_visibility(self.error_locator)

    @property
    def ele_popup(self)-> WebElement:
        return self.get_element_visibility(self.popup_locator)

