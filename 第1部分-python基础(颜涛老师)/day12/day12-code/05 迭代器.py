# s = "北京欢迎您"
# for c in s:
#     print(c)

# for i in 123:
#     print(i)
# 可迭代对象: str, list, tuple, set, f, dict
# 所有的以上数据类型中都有一个函数__iter__(), 所有包含了__iter__()的数据类型都是可迭代的数据类型 Iterable
# dir()来查看一个对象,数据类型中包含了哪些东西
# lst = [1,2,3]   # list
# # print(dir(lst))
# s = "王尼玛"
# print("__iter__" in dir(s))
# print("__iter__" in dir(lst))
# print("__iter__" in dir(123))

# list是一个Iterable.可迭代的
# lst = ["皇阿玛", "皇额娘", "容嬷嬷", "紫薇"]
# 获取迭代器
# it = lst.__iter__()
# # 迭代器往外拿元素. __next__()
# print(it.__next__())    # 皇阿玛
# print(it.__next__())    # 皇额娘
# print(it.__next__())    # 容嬷嬷
# print(it.__next__())    # 紫薇
# print(it.__next__())    # 迭代到最后一个元素之后. 再进行迭代就报错了

# lst = ["皇阿玛", "皇额娘", "容嬷嬷", "紫薇"]
# # 模拟for循环
# it = lst.__iter__()
# while True:
#     try:
#         name = it.__next__()
#         print(name)
#     except StopIteration: # 拿完了
#         break

lst = [1, 2, 3]
from collections import Iterable    # 可迭代的
from collections import Iterator    # 迭代器

# isinstence(对象, 类型) 判断xx对象是否是xxx类型的
# print(isinstance(lst, Iterable))
# print(isinstance(lst, Iterator))

# it = lst.__iter__()
# print(isinstance(it, Iterable)) # 判断是否是可迭代的 迭代器一定是可迭代的
# print(isinstance(it, Iterator)) # 迭代器里面一定有__next__(), __iter__()

# print("__iter__" in dir(lst))   # 确定是一个可迭代的
# print("__next__" in dir(lst))   # 确定不是一个迭代器

# f = open("01 今日内容大纲",mode="r", encoding="utf-8")
# print(isinstance(f, Iterable))
# print(isinstance(f, Iterator))

# 迭代器的特点:
#   1. 节省内存
#   2. 惰性机制
#   3. 只能往前拿. 不能反着拿
lst = ["哈哈", "呵呵"]
it = lst.__iter__()
it.__next__()
print(it.__next__())
print("我要吃黄瓜")
print(it.__next__())