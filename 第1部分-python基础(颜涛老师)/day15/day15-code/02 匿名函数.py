def func(n):
    return n * n

print(func(3))
a = func
a(3)
print(a.__name__)    # 查看函数的函数名
# lambda 匿名函数
# x 参数
#  : 后面是函数体(直接return的内容)
a = lambda x: x*x   # 一行搞定一个函数. 但是, 不能完成复杂的函数操作
print(a)
print(a(6))
print(a.__name__)

b = lambda x, y: x+y
print(b(1,3))
print(b.__name__)

# 语法: 变量 = lambda 参数: 返回值


