# -*- coding:utf-8 -*-
# @Time    : 2020/6/26 10:17
# @Author  : mmy
# @File    : indexpage
from webtest.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class IndexPage(BasePage):
    ele_user_locator=(By.XPATH,"//a[@href='/Member/index.html']")
    # ele_user_locator = (By.XPATH, "//img[@class='mr-5']//..")

    @property
    def ele_user(self) ->WebElement:
        return self.get_element_visibility(self.ele_user_locator)


if __name__ == '__main__':
    from webtest.pages.loginpage import LoginPage
    from selenium import webdriver
    driver = webdriver.Chrome()
    loginpage = LoginPage(driver)
    indexpage = IndexPage(driver)
    url = 'http://120.78.128.25:8765/Index/login.html'
    driver.get(url)
    loginpage.submit_login('18684720553', 'python')
    text = indexpage.ele_user.text
    print(text)


