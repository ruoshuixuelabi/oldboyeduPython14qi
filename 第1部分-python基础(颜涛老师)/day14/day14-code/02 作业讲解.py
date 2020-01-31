# 1.
# lst = ["alex", "sb", "taibai", "sb", "wusir","sb", "ritian", "sb"]
#
# new_lst = [e.upper() for e in lst if len(e) >= 3]
# print(new_lst)
#
# # 2.
# lst = [(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 2 == 1]
# print(lst)

# 3. M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
# print([i[2] for i in M])

# M = [3,6,9]
# print([[x-2, x-1,x] for x in M])

# 4.
# print([x*x for x in range(51) if x % 3 == 0])

# 5.
# print([(x, x + 1) for x in range(6)])

# 6.
# print([x for x in range(0, 20 ,2)])

# 7.
l1 = ['alex', 'WuSir', '老男孩', '太白']
print([l1[i] + str(i) for i in range(len(l1))])

# 9.
x = {
    'name':'alex',
    'Values':[{'timestamp':1517991992.94,'values':100,},
        {'timestamp': 1517992000.94,'values': 200,},
        {'timestamp': 1517992014.94,'values': 300,},
        {'timestamp': 1517992744.94,'values': 350},
        {'timestamp': 1517992800.94,'values': 280}
		],}

print([ [el['timestamp'], el['values']]for el in x['Values']])
