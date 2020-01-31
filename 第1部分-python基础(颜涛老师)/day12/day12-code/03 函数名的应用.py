# def func():
#     print("你吃了么?")
#
# # print(func)
# # a = func    # 函数名就是一个变量
# # print(a)
# # func()
# # a() # 就是一个函数的调用
#
# def a():
#     print("我吃了")
#
# func = a
# func()

# a = 8
# b = 7
# c = 1
# d = 3
# lst = [a, b , c, d]
# print(lst)
#
# def f1():
#     print("我是马化腾")
# def f2():
#     print("我是马云")
# def f3():
#     print("我是马赛克")
# def f4():
#     print("我是马蔚华")
#
# lst = [f1(), f2(), f3(), f4()]
# print(lst)


# 还可以作为函数的参数
# def func(food):
#     print("吃", food)
#
# a = "火锅"
# func(a)


# def func(fn):
#     fn()
#
# def gn():
#     print("我是火锅, 刚才有人要吃我")
# func(gn)    # 可以把函数作为参数, 传递给另一个函数


# def func():
#     def inner():
#         print("火锅不让吃了. 吃了上火")
#     return inner
# ret = func()    # 这里func()执行之后获取到的是inner函数
# ret()   # 这里是让inner函数执行

# 综上. 函数就是一个变量
