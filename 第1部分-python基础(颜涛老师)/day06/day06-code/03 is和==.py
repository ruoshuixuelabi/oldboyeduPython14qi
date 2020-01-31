# s = "alex 是 大 xx"
# abc = id(s)   # 得到内存地址
# print(abc)

# lst = ["大阳哥", "佳琪哥", "小花生", "燃哥"]
# print(id(lst))  # 就是一个内存地址. 毫无意义


# lst = ["周杰伦", "燃哥"]
# lst1 = ["周杰伦", "燃哥"]
# print(id(lst))
# print(id(lst1))

# s = "燃哥"
# s1 = "燃哥"
# # 小数据池. 会对字符串进行缓存, 为了节省内存
# print(id(s))
# print(id(s1))

# tu = ("燃哥", "周杰伦")
# tu1 = ("燃哥", "周杰伦")
# print(id(tu), id(tu1))

# dic = {"a": "b", "c":"d"}
# dic1 = {"a": "b", "c":"d"}
# print(id(dic), id(dic1))

# a = 10
# b = 10
# print(id(a), id(b))

# 布尔也有,
# a = True
# b = True
# print(id(a), id(b))

# -5
# a = 257
# b = 257
# print(id(a), id(b))

# a = "小威"
# b = "小威"
# print(id(a), id(b))

# 1. id() 查看内存地址
# 2. str 有小数据池的

# == is id
# == 判断. 左右两端是否相等和一致, 比较的是内容
# is 判断. 判断的是内存地址  id()的值来判断    内存地址

# lst = ["马化腾", "小威"]
# lst2 = ["马化腾", "小威"]
# print(lst == lst2)  # True
# print(lst is lst2)  # False


# s = "alex"
# print("1111111111")
# print("1111111111")
# print("1111111111")
# print("1111111111")
# print("1111111111")
# print("1111111111")
# print("1111111111")
# print("1111111111")
# print("1111111111")
#
# s2 = "alex"
# print(s == s2) # True
# print(s is s2)  # True. 小数据池

# s1 = "@akljflkasdjklfjkasdlfjklsdajfklsdajfklasdjkflasdjklfjsdaklfjsdakljfklasdjfklsdajfklsdajfklsdajklfsjadklfjsadklfjasdkljfklsdjfklsdjfklsdjfklsdjfklasdjfklasdjklfjasdklakljflkasdjklfjkasdlfjklsdajfklsdajfklasdjkflasdjklfjsdaklfjsdakljfklasdjfklsdajfklsdajfklsdajklfsjadklfjsadklfjasdkljfklsdjfklsdjfklsdjfklsdjfklasdjfklasdjklfjasdkl"
# s2 = "@akljflkasdjklfjkasdlfjklsdajfklsdajfklasdjkflasdjklfjsdaklfjsdakljfklasdjfklsdajfklsdajfklsdajklfsjadklfjsadklfjasdkljfklsdjfklsdjfklsdjfklsdjfklasdjfklasdjklfjasdklakljflkasdjklfjkasdlfjklsdajfklsdajfklasdjkflasdjklfjsdaklfjsdakljfklasdjfklsdajfklsdajfklsdajklfsjadklfjsadklfjasdkljfklsdjfklsdjfklsdjfklsdjfklasdjfklasdjklfjasdkl"
# print(id(s1), id(s2))
#
# s = "abc中def"
# print(s.title())



