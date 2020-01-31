



# def func():
#     global a    # a 不再是局部变量. 是全局变量
#     a = 30  # 把全局中的a重新赋值成30
#     print(a)
# func()
# print(a)

# a = 10
# def func1():
#
#     def func2():
#         nonlocal a  # 找局部作用域中 离他最近的那个变量引入进来
#         a = 20
#         print(a)
#     func2()
#     print(a)
# func1()

a = 1
def fun_1():
    a = 2
    def fun_2():
         def fun_3():
             nonlocal a
             a =  4
             print(a)
         print(a)
         fun_3()
         print(a)
    print(a)
    fun_2()
    print(a)
print(a)
fun_1()
print(a)


