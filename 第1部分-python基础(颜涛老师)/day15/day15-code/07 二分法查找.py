# lst = [11,22,33,44,55,66,77,88,99,123,234,345,456,567,678,789,1111]
# n = 567
# left = 0
# right = len(lst) - 1
# count = 1
# while left <= right:
#     middle = (left + right) // 2
#     if n > lst[middle]:
#         left = middle + 1
#     elif n < lst[middle]:
#         right = middle - 1
#     else:
#         print(count)
#         print("存在")
#         print(middle)
#         break
#     count = count + 1
# else:
#     print("不存在")
lst = [11,22,33,44,55,66,77,88,99,123,234,345,456,567,678,789,1111]

def binary_search(left, right, n):
    middle = (left + right)//2
    if left > right:
        return -1
    if n > lst[middle]:
        left = middle + 1
    elif n < lst[middle]:
        right = middle - 1
    else:
        return middle
    return binary_search(left, right, n)
print(binary_search(0, len(lst)-1, 65) )


def binary_search(lst, n):
    left = 0
    right = len(lst) - 1
    middle = (left + right) // 2
    if right <= 0:
        print("没找到")
        return
    if n > lst[middle]:
        lst = lst[middle+1:]
    elif n < lst[middle]:
        lst = lst[:middle]
    else:
        print("找到了")
        return
    binary_search(lst, n)
binary_search(lst, 65)


