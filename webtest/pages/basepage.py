# -*- coding:utf-8 -*-
# @Time    : 2020/6/26 10:16
# @Author  : mmy
# @File    : basepage

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def get_element_visibility(self,locator,timeout=20):
        try:
            return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print("没有找到元素")
            raise e

    def get_element_presence(self,locator,timeout=20):
        try:
            return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            print("没有发现元素")
            raise e

    def switch_window(self):
        current_win=self.driver.current_window_handle
        WebDriverWait(self.driver,20).until(EC.new_window_is_opened(current_win))
        all_win=self.driver.window_handles
        return self.driver.switch_to.window(all_win[-1])