#pytest.ini 可以修改 pytest 的默认行为
# pytest.ini 不能使用任何中文符号，包括汉字、空格、引号、冒号等等；

"""
1.更改默认命令行参数
将常用的命令行参数设置为默认，省去重复工作：
# pytest.ini

[pytest]
addopts = --capture=no,--result-log=reports/test1.log,--junit-xml=reports/xml_test.xml,--html=reports/html_test.html

2、注册mark标记
[pytest]
markers =
    demo : marks tests as demo
    smoke: marks tests as smoke

3、指定测试目录：testpaths 限定测试用例的搜索范围，只有在 pytest 范围指定文件目录参数或测试用例标识符时，该选项才会启用
  testpaths 指定的路径是以 testpaths 所在的目录为基准的相对路径
[pytest]
testpaths = test_path

4、更改测试用例收集规则
pytest 默认的用例收集规则：
    测试模块必须以 test_ 开头或以 _test 结尾；
    测试类必须以 Test 开头，且不能有 __init__() ；
    测试方法必须以 test_ 开头；
修改规则为：
    添加 check_ 开头的测试模块；
    添加 Check 开头的测试类；
    添加 check_ 开头的测试方法；

[pytest]
python_files = test_*  *_test  check_*
python_classes = Test*   Check*
python_functions = test_*  check_*


5、如果@pytest.mark.parametrize的argnames中的参数没有接收到任何的实参的话，用例的结果将会被置为SKIPPED,也可以通过empty_parameter_set_mark设置
    empty_parameter_set_mark=fail_at_collect=fail_at_collect

"""

import pytest

# 动态添加及获取ini配置参数
def pytest_addoption(parser):
    parser.addini('nice', type='bool', default=True, help='添加 ini 参数')


@pytest.fixture(autouse=True)
def get_ini(pytestconfig):
    """获取 ini 参数"""
    nice = pytestconfig.getini('nice')
    yield nice
    print(nice)



