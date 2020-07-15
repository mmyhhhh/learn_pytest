import pytest
from datetime import datetime, timedelta

testdata = [
(datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
(datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]

# 如果argnames包含多个参数，那么argvalues的迭代返回元素必须是可度量的（即支持len()方法），
# 并且长度和argnames声明参数的个数相等，所以它可以是元组/列表/字典等
@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected


def idfn(val):
    if isinstance(val, (datetime,)):
    # note this wouldn't show any hours/minutes/seconds
        return val.strftime("%Y%m%d")


@pytest.mark.parametrize("a,b,expected", testdata, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize( "a,b,expected", [
    pytest.param(datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1), id="forward"),
    pytest.param(datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1), id="backward"),],)
def test_timedistance_v3(a, b, expected):
    diff = a - b
    assert diff == expected


# 如果argnames包含多个参数，那么argvalues的迭代返回元素必须是可度量的（即支持len()方法），
# 并且长度和argnames声明参数的个数相等，所以它可以是元组/列表/字典等
@pytest.mark.parametrize('input,expectd', [(1, 2),[3,4]])  #参数有两个，那么argvalues返回的元素即解包后（此处是去掉列表中括号）是可迭代对象，即(1, 2),[3,4]，并且每一个对象的长度要与参数个数相等
def test_sample(input,expectd):
    print(input,expectd)
    assert input + 1 == expectd


#将指定参数的实参通过request.param重定向到和参数同名的fixture中

@pytest.fixture()
def max(request):
    return request.param - 1


@pytest.fixture()
def min(request):
    return request.param + 1


# 默认 indirect 为 False,当参数名与fixture函数名相同时，参数名替代fixture函数传入测试函数中
@pytest.mark.parametrize('min, max', [(1, 2), (3, 4)])
def test_indirect(min, max):
    assert min <= max


# min max 对应的实参重定向到同名的 fixture 中
@pytest.mark.parametrize('min, max', [(1, 2), (3, 4)], indirect=True)
def test_indirect_indirect(min, max):
    assert min >= max


# 只将 max 对应的实参重定向到 fixture 中
@pytest.mark.parametrize('min, max', [(1, 2), (3, 4)], indirect=['max'])
def test_indirect_part_indirect(min, max):
    assert min == max

@pytest.mark.parametrize('test_input', [1, 2, 3])
@pytest.mark.parametrize('test_output, expected', [(1, 2), (3, 4)])
def test_mul(test_input,test_output,expected):
    print('打印结果',test_input, test_output, expected)
    pass

# 为了提高代码的复用性，我们在写用例的时候，会用到函数，然后不同的用例去调用这个函数。比如登录操作，大部分的用例都会先登录，那就需要把这个登录单独抽出来写个函数，其他用例全部的调用这个登录函数就行。
#
# 但是登录的账号不能写死，有时候要用账号1登录、执行用例1，用账号2登录执行用例2，所以需要对函数传参
