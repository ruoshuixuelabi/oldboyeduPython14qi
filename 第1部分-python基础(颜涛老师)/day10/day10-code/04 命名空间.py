# a = "123"   # 全局
# b = 36  # 全局
# def func(): # 全局
#     c = "马化腾"   # 局部
#
# def func2():
#     print(c)

a = 10
def func():
    a = 20
    print(a)    # 就近原则
    print(globals())  # globals() 获取到全局作用域(内置,全局)中的所有名字
    print(locals())  # locals() 查看当前作用域中的所有名字
func()




