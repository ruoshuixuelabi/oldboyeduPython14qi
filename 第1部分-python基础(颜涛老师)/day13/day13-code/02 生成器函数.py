# def func():
#     print("我是周杰伦")
#     yield "昆凌"  # 函数中包含了yield, 当前这个函数就不再是普通的函数了. 是生成器函数
#     print("我是王力宏")
#     yield "李云迪???"
#     print("我是笛卡尔积")
#     yield "笛卡尔积是谁"
    # print("你好啊") # 最后一个yield之后如果再进行__next__() 会报错
# g = func()
# print(g.__next__())
# print(func().__next__())
#
# g1 = func()
# g2 = func()
# print(g1.__next__())
# print(g1.__next__())
#
# print("==============")
# print(g2.__next__())

#
# g = func()  # 通过函数func()来创建一个生成器
# print(g.__next__()) # 周杰伦
# print(g.__next__()) # 王力宏
# print(g.__next__()) # 笛卡尔积
# print(g.__next__())

# return 直接返回结果. 结束函数的调用
# yield 返回结果.可以让函数分段执行
#
# def func():
#     lst = []
#     for i in range(1,100001):
#         lst.append("衣服%s" % i)
#     return lst
#
# def gen():
#     i = 1
#     while i < 100001:
#         yield "衣服%s" % i
#         i = i + 1
# g = gen()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

#
# def func():
#     yield 11
#     yield 22
#     yield 33
#     yield 44
#
#
# g = func()  # 拿到的是生成器. 生成器的本质是迭代器. 迭代器可以被迭代 生成器可以直接for循环
#
# for i in g:
#     print(i)    # 本质上执行的是__next__()
#
# it = g.__iter__()
# while True:
#     try:
#         print(it.__next__())
#     except StopIteration:
#         break
