user_list=[
        {"name": "alex", "hobby": "抽烟"},
        {"name": "alex", "hobby": "喝酒"},
        {"name": "alex", "hobby": "烫头"},
        {"name": "wusir", "hobby": "喊麦"},
        {"name": "wusir", "hobby": "街舞"},
{"name": "alex", "hobby": "泡吧"},
        {"name":"太白", "hobby":"开车"}
         ]
# [{"name": "alex", "hobby_list": ["抽烟","喝酒","烫头","泡吧"]},{"name": "wusir", "hobby_list": ["喊麦", "街舞"]},]

result = [] # {'name': 'alex', 'hobby_list': ['抽烟']}
for user in user_list:
    # 1.判断是否在result里面存在了这个人, 如果存在. 把hobby_list添加一个hobby
    # 2.不存在. 创建一个新字典
    for new_user in result:
        if user['name'] == new_user['name']:
            new_user['hobby_list'].append(user['hobby'])
            break
    else:
        dic = {}
        dic["name"] = user['name']
        dic['hobby_list'] = [user['hobby']]
        result.append(dic)
print(result)



