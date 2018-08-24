#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michel', 'Bob', 'Tracy']
print(classmates)
a = len(classmates)
print(a)

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
list1 = classmates[0]
list2 = classmates[1]
print(list1, list2)

# 最后一个元素的索引  len(classmates) - 1 或者 -1
last_1 = classmates[len(classmates)-1]
last_2 = classmates[-1]
print(last_1)
print(last_2)

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('bolt')
append_1 = classmates
print(append_1)

# 插入
classmates.insert(1, 'wang')
insert_1 = classmates
print(insert_1)
# 删除
classmates.pop()   # 删除末尾元素
pop_1 = classmates
classmates.pop(2)  # 删除指定的元素
pop_2 = classmates
print(pop_1)
print(pop_2)

# 替换
classmates[0] = 'abc'
print(classmates)

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改,list是[],tuple是()
t = (1, 2)
print(t)

# 练习 请用索引取出下面list的指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    ]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])