# -*- coding: UTF-8 -*-
import unicodedata
#创建自定义函数is_number()方法来判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
#测试字符串和数字
print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('-1.37'))
print(is_number('1e3'))
#测试Unicode
#阿拉伯语 5
print(is_number('٥'))  # False
#泰语 2
print(is_number('๒'))  # False
#中文数字
print(is_number('四')) # False
#版权号
print(is_number('©'))  # False
#s.isdigit:
#True:Unicode数字,bytes数字(单音节),全角数字(双音节),罗马数字
#False:汉字数字
#Error:无

#s.isdecimal()
#True:Unicode数字,全角数字(双音节)
#False:罗马数字,汉字数字
#Error:byte数字(单音节)

#s.isnumeric()
#True:Unicode,全角数字(双音节),罗马数字,汉子数字
#False:无
#Error:byte数字(单字节)