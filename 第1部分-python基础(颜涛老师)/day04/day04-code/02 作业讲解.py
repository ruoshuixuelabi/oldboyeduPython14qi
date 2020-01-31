# 1.请输出 name 变量对应的值中 "e"  所在索引位置?
name = "aleX leNb"

# e1 = name.find("e", 0,5 )
# print(e1)
#
# e2 = name.find("e",5 )
# print(e2)

# count = 0
# while count < len(name):
#     if name[count] == 'e':
#         print(count)
#     count = count +1

# s1 = name[:1]
# s2 = name[1:]
# print(s1.upper()+s2)
#
# name.replace("a", "A")

# s="asdfer"
# for c in s: # c :charactor
#     print(c)
#
# for c in s:
#     print(s)
#
# for c in s:
#     print("sb"+c)

# s="321"
# for c in s:
#     print("倒计时%s秒" % c)
# else:
#     print("出发!")

# content = input("请输⼊内容:") ⽤户输⼊：5+9 或5+ 9 或5 + 9，然后进⾏分割再进⾏计算
# content = input("请输⼊内容:")
# lst = content.split("+")
# s1 = lst[0]
# s2 = lst[1]
# a1 = int(s1)
# a2 = int(s2)
# print(a1+a2)

# content = input("请输⼊内容：")   # 如fhdau234slfh98769fjdba
# count = 0
# for c in content:
#     if c.isdigit():
#         count = count + 1
# print(count)
#
# while 1:
#     lu = input("请输入ABC:").strip().upper()
#     if lu == 'A':
#         content = input("请选择公交车还是步行:")
#         if content == '公交车':
#             print("10分钟到家")
#             break
#         elif content == '步行':
#             print("20分钟到家")
#             break
#         else:
#             print("我也不知道怎么办")
#     elif lu == 'B':
#         print("走小路回家")
#         break
#     elif lu == 'C':
#         print("绕路回家")
#         content = input("去哪儿浪啊?")
#         if content == '网吧':
#             print("两个小时到家，妈妈已做好了战⽃准备。")
#         else:
#             print("一个半小时到家，爸爸在家，拿棍等你。")
#     else:
#         print("你是不是傻. ")


# 1 - 2 + 3 - 4  ... + 99  去掉88
# count = 1
# sum = 0
# while count < 100:
#     if count == 88:
#         count = count + 1
#         continue
#     if count %2 == 0:# 偶数
#         sum = sum - count
#     else:
#         sum = sum + count
#     count = count + 1
# print(sum)


# s = "明天到操场操到天明"
# s1 = s[::-1]
# if s == s1:
#     print("回文")
# else:
#     print("不是回文")
#
# content = input("请输入一个字符串:")
# digit_num = 0
# upper_c_num = 0
# lower_c_num = 0
# other = 0
#
# for c in content:
#     if c.isdigit():
#         digit_num += 1
#     elif c.isupper():
#         upper_c_num += 1
#     elif c.islower():
#         lower_c_num += 1
#     else:
#         other += 1
#
# print(digit_num)
# print(upper_c_num)
# print(lower_c_num)
# print(other)

# name = input("请输入你的名字:")
# address = input("请输入你的地点:")
# hobby = input("请输入你的爱好:")
# print("敬爱可亲的{name}, 喜欢在{address}干{hobby}".format(name=name, address=address, hobby=hobby))

s = "欧阳娜娜"
ss = ""
for c in s:
    ss = ss + c
    print(ss)
