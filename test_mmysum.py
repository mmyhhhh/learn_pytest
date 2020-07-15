# -*- coding:utf-8 -*-
# @Time    : 2020/6/25 16:02
# @Author  : mmy
# @File    : test_mmysum

import pytest
from demo import MmySum
mmysum=MmySum()

class TestMmySum:

    def test_int(self):
        result=mmysum.sum_abs(1,2)
        assert 1+2==result


