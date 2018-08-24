#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输入用户年龄，根据年龄打印不同的内容
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

# else if
age1 = 3
if age1 >= 18:
    print('adult')
elif age1 >= 6:
    print('teenager')
else:
    print('kid')

# input()
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果： 
# 

height = 1.75
weight = 80.5
bmi = weight / pow(height, 2)

if bmi < 18.5:
    print('过轻')
elif (bmi >= 18.5) and (bmi < 25):
    print('正常')
elif (bmi >= 25) and (bmi < 28):
    print('过重')
elif (bmi >= 28) and (bmi < 32):
    print('肥胖')
elif (bmi > 32):
    print('严重肥胖')
