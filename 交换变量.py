# -*- coding: UTF-8 -*-

#使用临时变量
x = input('输入x值:')
y = input('输入y值:')

temp = x
x = y
y = temp

print('交换后x的值为:{}'.format(x))
print('交换后y的值为:{}'.format(y))

#不使用临时变量
x, y = y, x

print('再次交换后的x为{},y为{}'.format(x,y))