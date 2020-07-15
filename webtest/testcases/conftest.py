import pytest
from selenium import webdriver

from webtest.pages.indexpage import IndexPage
from webtest.pages.loginpage import LoginPage


@pytest.fixture(scope='class')
def init_driver():
    driver = webdriver.Chrome()
    url = 'http://120.78.128.25:8765/Index/login.html'
    driver.get(url)
    loginpage = LoginPage(driver)
    indexpage = IndexPage(driver)
    yield (driver,loginpage,indexpage)
    driver.quit()

@pytest.fixture()
def setup(init_driver):          #fixture作为参数直接传入另一个fixture中
    driver,loginpage,indexpage=init_driver
    driver.refresh()

@pytest.fixture()
def login(request,init_driver):
    driver,loginpage,indexpage=init_driver
    loginpage.submit_login(request.param['phone'],request.param['pwd'])
    print('登录成功')

