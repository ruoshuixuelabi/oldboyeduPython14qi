# def chi(good_food, bad_food,drink, ice, jiu):
#     print("我要吃", good_food, bad_food)
#
# chi("盖浇饭", "辣条")

# 位置参数 > *动态参数 > 默认值参数


# def chi( *food, a, b): # 可以传入任意的位置参数
#     print("我要吃", food)  # 动态参数接收到的是tuple类型的数据
#
# chi("盖浇饭", "辣条", "面条")
# def func(a, b, c, *args, d = 5):
#     print(a, b, c, d, args)
#
# func(1,2,3)
# func(1,2,3,4,5,6,7, d ="马大哈")

# def chi(*food):
#     print("我要吃", food)

#　写函数. 给函数传递任意个整数. 返回这些数的和
# def he(*n):
#     sum = 0
#     for e in n:
#         sum += e
#     return sum
# print(he(5))


# 动态接收关键字参数
#  *位置参数
# **关键字参数
# def func(**food):   # **food动态接收关键字参数
#     print(food) # 接收到的是字典
#
# func(good_food="盖浇饭", bad_food="辣条", drink="冰封")

# 关键字参数一定在位置参数后面
# 位置参数 > *args > 默认值 > **kwargs

# 这个函数可以接收所有的参数(无敌的)
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func(1, 2, 5, 6, name="taibai",age=18, sex="不详")

# 把列表中的每一个元素作为参数, 传递给函数. 一次都传过去

# def func(*args, **kwargs):  # *表示聚合,所有的位置参数, 聚合成元组 **聚合成字典
#     print(args)
#     print(kwargs)
#
#
# # lst = ["马虎疼", "大洋哥", "小花生", "毛尖妹妹"]
# # func(*lst)  # 实参, 打散, 迭代产生的
#
# dic = {"name":"太白", "alex":"wuse"}
# func(**dic) # 把字典打散. 以key=value形式进行传参


# def func(a, b):
#     """
#     计算a+b的和, 返回一个数
#     :param a: 第一个数
#     :param b: 第二个数
#     :return: 返回计算之后的和
#     """
#     return a + b

# 定义函数
# def 函数名(形参):  1.位置参数, 2, *args, 3.默认值参数, 4. **kwargs
#     函数体   return 返回值
# 函数名(实参)    1. 位置参数. 2.关键字参数. 3. 混合参数,
