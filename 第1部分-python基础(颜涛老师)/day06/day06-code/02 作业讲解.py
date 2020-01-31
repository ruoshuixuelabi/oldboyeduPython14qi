# dic = {"a": "俩继承", "b":"马化腾"}
# for k in dic.keys():
#     print(k)
#
# for k in dic:
#     print(k)
#
# for k, v in dic.items():
#     print(k, v)


av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

# 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个  元素：'量很大'。
# av_catalog['欧美']["www.youporn.com"].insert(1, "量很大")
# print(av_catalog)

# 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog['欧美']['x-art.com'].remove("全部收费,屌丝请绕过")
# print(av_catalog)

# 在此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表中添加"金老板最喜欢这个"
# av_catalog['欧美']['x-art.com'].append("金老板最喜欢这个")
# print(av_catalog)

# 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog["日韩"]['tokyo-hot'][1] = av_catalog["日韩"]['tokyo-hot'][1].upper()
# print(av_catalog)

# 给'大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog['大陆']["1048"] = ['一天就封了']

# 删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
# av_catalog['欧美'].pop("letmedothistoyou.com")
# print(av_catalog)


# 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog['大陆']["1024"][0] = av_catalog['大陆']["1024"][0] + "可以爬下来"
# print(av_catalog)


# 4. "k:1|k1:2|k2:3|k3:4"
# s = 'k:1|k1:2|k2:3|k3:4'
# lst = s.split("|")
# dic = {}
# for el in lst:
#     # print(el)   # [k,1]
#     k, v = el.split(":")
#     dic[k] = int(v)
# print(dic)


# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，
# 将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}

# li= [11,22,33,44,55,66,77,88,99,90]
# dic = {"k1":[], "k2":[]}
#
# for el in li:
#     if el > 66:
#         dic['k1'].append(el)
#     elif el < 66:
#         dic["k2"].append(el)
#     else:
#         pass
# print(dic)

# li= [11,22,33,44,55,66,77,88,99,90]
# dic = {}
# for el in li:
#     if el > 66:
#         dic.setdefault("k1", []).append(el) # 1. 新增, 2. 查询
#     else:
#         dic.setdefault("k2", []).append(el)  # 1. 新增, 2. 查询
# print(dic)


# 6.
# goods = [{"name": "电脑", "price": 1999},
#          {"name": "鼠标", "price": 10},
#          {"name": "游艇", "price": 20},
#          {"name": "美女", "price": 998}]
#
# for i in range(len(goods)):
#     good = goods[i]
#     print(i+1, good['name'], good['price'])
#
# while 1:
#     content = input("请输入你要买的商品:")
#     if content.upper() == "Q":
#         break
#     index = int(content) - 1    # 索引
#     if index > len(goods) - 1 or index < 0:  # 调试
#         print("输入有误. 请重新输入:")
#         continue
#     print(goods[index]['name'], goods[index]['price'])








