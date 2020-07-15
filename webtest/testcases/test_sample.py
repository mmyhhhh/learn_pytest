import pytest

# def func(x):
#     return x + 1
#
# def test_answer():
#     assert func(3) == 5



# def f():
#     raise SystemExit(1)
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

#在类中对测试分组时需要注意的是，每个测试都有一个唯一的类实例。
# 让每个测试共享同一个类实例对测试隔离非常不利，并且会导致测试失败
#不太明白什么意思

# class TestClassDemoInstance:
#     def test_one(self):
#         assert 0
#     def test_two(self):
#         assert 0

# pytest -k TestClassDemoInstance -q  #-k选项允许你使用表达式指定希望执行的测试用例
from _pytest import tmpdir


# def test_needsfiles(tmpdir):
#     print(tmpdir)
#     assert 0

# #tmp_path是一个用例级别的fixture，其作用是返回一个唯一的临时目录对象（py.path.local），它提供os.path的方法
# #其实，tmpdir也调用了tmp_path，只是对返回值做了一次py.path.local()封装：
#
# CONTENT = "content"
# def test_create_file(tmpdir):
#     p = tmpdir.mkdir("sub").join("hello.txt")  # 创建子文件夹，并新建文件
#     p.write(CONTENT)
#     assert p.read() == CONTENT
#     assert len(tmpdir.listdir()) == 1  # iterdir() 迭代目录，返回列表
#     assert 0  # 为了展示，强制置为失败
"""
第几条用例执行失败的话停止此次测试:
# pytest -x   # stop after first failure  第一条执行失败后停止
# pytest --maxfail=2   # stop after two failures  第二条执行失败后停止
"""

"""
执行整个模块用例
pytest test_mod.py

执行整个测试文件夹用例：Run tests in a directory
pytest testing/

根据用例名称执行用例，可以进行逻辑运算（包括filenames, class names and function names as variables）
pytest -k "MyClass and not method"

通过节点id来执行测试用例，用::分隔
pytest test_mod.py::TestClass::test_method

通过mark标记来执行测试用例
pytest -m slow  #执行所有被@pytest.mark.slow装饰的测试用例

从包运行测试：Run tests from packages
pytest --pyargs pkg.testing
"""


#执行结果总结概括参数
#pytest -ra   r选项接受后面的多个字符，上面使用的表示“除传递之外的所有”。
# • f - failed
# • E - error
# • s - skipped
# • x - xfailed
# • X - xpassed
# • p - passed
# • P - passed with output
# Special characters for (de)selection of groups:
# • a - all except pP
# • A - all
# • N - none, this can be used to display nothing (since fE is the default)
@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

#