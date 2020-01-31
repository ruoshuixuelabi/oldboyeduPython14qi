# s = "alex and wusir and taibai"
# s1 = s.capitalize()  # 首字母大写
# print(s)    # 原字符串不变
# print(s1)

# s = "Alex is not a Good Man. "

# print(s.upper())
# print(s.lower())

# 在程序需要判断不区分大小写的时候. 肯定能用上
#
# while True:
#     content = input("请喷:")
#     if content.upper() == 'Q':
#         break
#     print("你喷了:", content)

# s = "taiBai HenBai feicahngBai"
# print(s.swapcase()) # 大小写转换

# s = "al麻花藤ex and wu sir sir se"
# print(s.title())

# s = "麻花藤"
# print(s.center(9, "*"))

# username = input("用户名:").strip()    # 去掉空格.
# password = input("密码:").strip()     # 去掉空格
# if username == 'alex' and password == '123':
#     print("登录成功")
# else:
#     print("登录失败")

# s = "*******呵a呵呵呵****************"
# print(s.strip("*"))   # strip去掉的是左右两端的内容. 中间的不管


# s = "alex wusir alex sb taibai"
# s1 = s.replace("alex", "晓雪") # 原字符串不变
# print(s1)
# # 去掉上述字符串中的所有空格
# s2 = s.replace(" ", "")
# print(s2)


# s3 = s.replace("alex", "sb", 2)
# print(s3)
#
# s = "alex_wuse_taibai_bubai"
# lst = s.split("_taibai_")    # 刀是_  切完的东西是列表. 列表装的是字符串
# print(lst)


# s = "我叫{}, 我今年{}岁了, 我喜欢{}".format("sylar", 18, "周杰伦的老婆")
# print(s)

# 可以指定位置
# s = "我叫{1}, 我今年{0}岁了, 我喜欢{2}".format("sylar", 18, "周杰伦的老婆")
# print(s)

# s = "我叫{name}, 我今年{age}岁了, 我喜欢{mingxing}".format(name="sylar", mingxing="汪峰的老婆", age=18)
# print(s)

# 你喜欢用哪个就用哪个


# s = "汪峰的老婆不爱汪峰"

# print(s.startswith("汪峰"))   # 判断字符串是否以xxx开头
# print(s.endswith("爱妃"))     # 判断字符串是否以xxx结尾
# print(s.count("国际章"))   # 计算xxx在字符串中出现的次数

# print(s.find("汪峰", 3))    # 计算xxx字符串在原字符串中出现的位置, 如果没出现返回 -1
# print(s.index("国际章"))    # index中的内容如果不存在. 直接报错

# s = "abc123"
# print(s.isdigit())  # 判断字符串是否由数字组成
# print(s.isalpha())  # 是否由字母组成
# print(s.isalnum())  # 是否由字母和数字组成

# s = "二千136万萬"
# print(s.isnumeric())    # 数字

# s = "你今天喝酒了么"
# i = len(s)  #  print() input() len() python的内置函数
# print(i)
#
# i = s.__len__() # 也可以求长度 len()函数执行的时候实际执行的就是它
# print(i)

# 把字符串从头到尾进行遍历
# s = "晓雪老师.你好漂亮"
# print(len(s))   # 长度是:８　索引到7
# 1. 使用while循环来进行遍历
# count = 0
# while count < len(s):
#     print(s[count])
#     count = count + 1

# 2. 用for循环来遍历字符串
# 优势:简单
# 劣势:没有索引
# for c in s: # 把s中的每一个字符交给前面的c 循环
#     print(c)

# 语法:
#     for bianliang  in  可迭代对象:
#         循环体











