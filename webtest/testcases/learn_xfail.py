import pytest
#
# canshu = [{"user":"amdin", "psw":"111"}]
#
# @pytest.fixture(scope="module")
# def login(request):
#     user = request.param["user"]
#     psw = request.param["psw"]
#     print("正在操作登录，账号：%s, 密码：%s" % (user, psw))
#     if psw:
#         return True
#     else:
#         return False

@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    print(request.param)
    return request.param


def test_data(data_set):
    pass


if __name__ == '__main__':
    pytest.main(['-vs', 'test_fixture_marks.py'])


