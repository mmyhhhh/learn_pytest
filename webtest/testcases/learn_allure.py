#allure 测试报告学习
#allure是一款轻量级灵活的开源测试报告框架，可以结合TESTNG、pytest、Junit等测试框架使用
#windows需要先安装allure，然后对应测试框架再安装插件.下载对应python的allure框架 allure-commandline，解压，进入bin文件夹，运行allure.bat，然后将bin目录配置到环境变量中，
# 注意，如果此时启动着pycharm，需要退出重启，在pycharm中的terminal终端上配置的环境变量才会生效
#结合pytest用，然后安装插件，安装命令：pip install allure-pytest

#使用方法
"""
allure 的几个特性：
@allure.feature # 用于描述被测试产品需求
@allure.story # 用于描述feature的用户场景，即测试需求
with allure.step # 用于描述测试步骤，将会输出到报告中
allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
语法： allure.attach(body, name, attachment_type, extension)
body：要显示的内容（附件）
name：附件名字
attachment_type：附件类型，是 allure.attachment_type 里面的其中一种：TEXT PNG JPG MP4 PDF JSON XML 等等
extension：附件的扩展名（比较少用）
@pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤

"""
import pytest
import allure

"""
运行用例的时候，加入 --alluredir=用例执行结果文件夹 命令选项，执行用例，allure结果会保存在设置的文件夹中，例如：--alluredir=./webtest/results
注意：allure文件夹使用相对路径，如果使用绝对路径，会在生成结果文件夹目录上一层生成一个全目录文件夹，例如：UsersAdministratorPycharmProjectslearn_pytestwebtest
"""

"""
执行完用例后，在终端输入 allure serve alluredir路径生成测试报告，报告会自动在默认浏览器打开
"""