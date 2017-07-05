# -*- coding: UTF-8 -*-

num = float(input('请输入一个数字:'))
if num>0:
#支持正数
    num_sqrt = num ** 0.5
    print('%0.3f的平方根为%0.3f'%(num,num_sqrt))
else:
#支持正数,负数,复数
    import cmath #导入复数数学模块
    num_sqrt = cmath.sqrt(num)
    print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real,num_sqrt.imag))