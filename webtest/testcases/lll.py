from operator import add

import pytest



#fixture 的应用方法：1、作为test的参数使用

@pytest.fixture()
def before():
    print('开始执行用例')

def test_1(before):
    print('执行用例test2')

def test_2(before):
    print('执行用例test2')
    assert 1

@pytest.fixture(scope='module',autouse=True) # 当autouse=True时，不用标记，执行用例时会自动先执行此特征函数，class级别的时候，还是会每个函数都执行（需要再确认）
def after():
    # print('用例执行完！！！')
    yield
    print('测试结束')

#方法2：@pytest.mark.usefixtures("before")

@pytest.mark.usefixtures('before')  #越接近函数名的装饰器越先执行
def test_3():
    print('执行用例test3')
    assert 2


#方法3：用autos调用fixture

def test_4():
    print('执行用例4')
    assert 3


# pytest 参数化
# 1). @pytest.mark.parametrize("参数名bai",["01_值1","02_值2"])
# 2). @pytest.mark.parametrize("参1，参2",[("01_参1的值du","01_参2的值"),("02_参1的值","02_参2的值")])

name_list=['lili','hello','sophia']
@pytest.mark.parametrize('name',name_list)
def test_name(name):
    print (name)


# data=['158','ghfjk','dgjslkk']
#
# @pytest.mark.parametrize('mmy',data,ids=['data[d]' for d in range(len(data))] )
def test_mmy(mmy):
    print(mmy)
    assert mmy in ['158','ghfjk','dgjslkk']


@pytest.mark.parametrize('mmy,lucy',[('158','ghfjk'),('160','很快就扣')])  #其中的两个参数名分别对应列表中每个元组子值里的一个子值，例如：mmy对应158.lucy对应ghfjk
def test_name(mmy,lucy):
    print(mmy)
    print(lucy)


import time
t0 = time.time()
time.sleep(1)
name = 'processing'

# 以 f开头表示在字符串内支持大括号内的python 表达式
print('{name} done in {time.time() - t0:.2f} s')

data = [(1,2,3), (4,5,9), ('1', '2', '12')]
ids = ['data{d}' for d in range(len(data))] # => 生成与数据数量相同的名称列表
@pytest.mark.parametrize('a, b, c', data, ids=ids)
def test_add(a, b, c):
    print('\na,b,c的值:{a},{b},{c}')
    assert add(a, b) == c