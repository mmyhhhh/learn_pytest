import pytest

if __name__ == '__main__':
    pytest.main(['--capture=no','--result-log=reports/test1.log','--alluredir=results','--html=reports/html_test.html'])