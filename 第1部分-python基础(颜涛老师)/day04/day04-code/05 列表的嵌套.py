lst = [1, "太白", "wusir", ["麻花疼", ["可口可乐"], "王剑林"]]

# print(lst[3][1][0])
# lst[3][1].append("芬达")
# print(lst)
lst[2] = lst[2].capitalize()
print(lst)

lst[1] = lst[1].replace("白", "黑")
print(lst)