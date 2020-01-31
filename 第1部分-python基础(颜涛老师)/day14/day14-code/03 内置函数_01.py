# def func():
#     a = 10
#     print(locals())  # 当前作用域中的内容
#     print(globals())  # 全局作用域中的内容
#     print("今天内容很简单")
# func()


# for i in range(20,15,-3):
#     print(i)

# lst = ["大阳哥", "喜欢", "私密的徒步"]
# it = iter(lst)  #  __iter__()
# print(it.__next__())
# print(next(it)) # __next__()
# print(next(it))
# print(next(it))

# print("李嘉诚", "黄花菜", "马云", sep="*", end="大阳哥") # seperator
# input("提示语")

# hash算法:
    # 目的是唯一性
    # dict 查找效率非常高, hash表.用空间换的时间 比较耗费内存

# s = "大阳哥"
# print(hash(s))
# a = 12
# print(hash(a))

# lst = [1,2,3,4,5,6,7]
# # print(hash(lst))    # 列表是不可哈希的
# print(hash((1,)))
# print(hash("呵呵"))
# print(hash("哈哈"))

# 让用户输入一个要导入的模块
# import os
# name = input("请输入你要导入的模块:")
# __import__(name)    # 可以动态导入模块

# print(help(str))

# print(dir(str))

# a = 11.25
# print(type(a))

# bin() 把一个十进制的数, 转换成二进制
# print(bin(10))  # 二进制
# print(hex(10))  # 十六进制
# print(oct(10))  # 八进制


# a = 10
# print(callable(a))
#
# def func():
#     print("马化腾")
# print(callable(func))   # 函数是可以被调用的

# s = input("请输入a+b:")
# print(eval(s))  # 可以动态的执行代码. 代码必须有返回值

# s = "25*4"
# a = eval(s) # 运算
# print(a)

# s = "for i in range(10): print(i)"
# a = exec(s) # exec 执行代码不返回任何内容
# print(a)

# 动态执行代码
# exec("""
# def func():
#     print(" 我是周杰伦")
# """ )
# func()

# code1 = "for i in range(10): print(i)"
# com = compile(code1, "", mode="exec")   # compile并不会执行你的代码.只是编译
# exec(com)   # 执行编译的结果
#
# code2 = "5+6+7"
# com2 = compile(code2, "", mode="eval")
# print(eval(com2))
#
# code3 = "name = input('请输入大阳哥的名字:')"
# com3 = compile(code3, "", mode="single")
# exec(com3)
# print(name)


# print(abs(-2))  # 绝对值
# print(abs(2))

# print(divmod(20,3)) # 求商和余数

# print(round(4.50))   # 五舍六入 => 四舍五入

# print(pow(10,2,3))  # 如果给了第三个参数. 表示最后取余

# print(sum([1,2,3,4,5,6,7,8,9,10]))  # 求和

# lst = "你好啊"
# it = reversed(lst)   # 不会改变原列表. 返回一个迭代器, 设计上的一个规则
# print(list(it))

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[1:3:1])
#
# s = slice(1, 3, 1)  #  切片用的
# print(lst[s])


# name = "你好. \n我叫%s周润发" % "李嘉诚"
# print(name)
# print(repr(name))   # 原样输出,过滤掉转义字符 \n \t \r 不管百分号

# print(ord('a')) # 97, 返回字母a在编码表中的码位
# print(ord('中')) # 20013 中国的中字在编码表中的位置

# print(chr(65)) # 已知码位. 计算字符
# print(chr(20018))
#
# for i in range(65536):
#     print(chr(i), end=" ")

# print(ascii("房"))

# s = "李嘉诚的爸爸"
# a = s.encode("UTF-8")
# print(a)
# print(a.decode("GBK"))


# bs = bytes("大阳哥今天很厉害", encoding="utf-8")
# print(bs.decode("utf-8"))

# ret =  bytearray("alex" ,encoding ='utf-8')
# print(ret[0])
# ret[0] = 65
# print(str(ret))

# s = memoryview("麻花藤".encode( "utf-8")) # 查看内存
# print(s)



