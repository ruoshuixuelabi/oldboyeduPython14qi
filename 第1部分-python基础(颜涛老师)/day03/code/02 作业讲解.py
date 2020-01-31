# 猜字游戏
# count = 1
# n = 66
# while count <= 3:
#     num = input("你猜一下")
#     if int(num) > n:
#         print("猜大了")
#     elif int(num) < n:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break
#     # 没猜对
#     print("你已经猜了%d次了" % count)
#     count = count + 1
# else:
#     print("愚蠢. 绝对的愚蠢")

# 1234568910
# count = 1
# while count <= 10:
#     if count != 7:
#         print(count)
#     count = count + 1
#
# count = 1
# while count <= 10:
#     if count == 7:
#         # count = 8
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# 1-2+3-4+5-6....+99
# sum = 0
# count = 1
# while count < 100:
#     if count%2 == 0:    # 偶数
#         sum = sum - count
#     else:   # 奇数
#         sum = sum + count
#     count = count + 1
# print(sum)

# 用户登录, 用户名:alex, 密码:sb
# count = 1
#
# while count <= 3:
#     username = input("请输入你的用户名:")
#     password = input("请输入你的密码:")
#     if username == 'alex' and password == 'sb':
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#
#     print("还剩%d次机会" % (3 - count))
#     count = count + 1
# else:
#     print("蠢. ")

# 广告
ad = input("请输入你的广告标语:")
if "最" in ad or '国家级' in ad or '第一' in ad or '稀缺' in ad:
    print("不合法")
else :
    print("合法")

