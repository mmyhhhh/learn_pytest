from configparser import ConfigParser

ccf=ConfigParser()
ccf.read(r'C:\Users\Administrator\PycharmProjects\learn_pytest\webtest\testcases\learn.ini',encoding='utf-8')
value=ccf['section']['markers']
# value=eval[value]
print(value,type(value))
