# s = "alex马"
# 想要存储.必须进行编码

# encode() 编码之后的内容是bytes类型的数据

# 30个字节 10个字. 每个字3个字节
# b'\xe6\x9d\x8e\xe5\x98\x89\xe8\xaf\x9a\xe7\x9a\x84\xe5\x84\xbf\xe5\xad\x90\xe8\xa2\xab\xe7\xbb\x91\xe6\x9e\xb6\xe4\xba\x86'
# bs = s.encode("UTF-8")   # 把字符串编码成UTF-8的形式
# print(bs)

# 英文:编码之后的结果是英文本身
# 中文:编码之后UTF-8 下. 一个中文3个字节


# s = "饿了么"
# bs = s.encode("GBK")    # b'\xb6\xf6\xc1\xcb\xc3\xb4' GBK 一个中文:２个字节
# print(bs)

# s = "中"
# print(s.encode("utf-8"))
# print(s.encode("GBK"))

# decode()解码

# bs = b'\xb6\xf6\xc1\xcb\xc3\xb4'    # 从别人那里读到的   GBK
#
# # 编程人认识的东西
# s = bs.decode("GBK")    # 解码之后是字符串, 用什么编码就用什么解码
# print(s)

# GBK => utf-8
bs = b'\xb6\xf6\xc1\xcb\xc3\xb4'
# 先解码成unicode字符串
s = bs.decode("GBK")
# 在把字符串编码成UTF-8
bss = s.encode("UTF-8")
print(bss)


