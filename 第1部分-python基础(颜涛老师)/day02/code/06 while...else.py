
count  = 1
while count  <= 10:
    print( count)
    count = count + 1
    if count == 5:
        break   # 彻底停止循环. 不会执行后面的else
else:   # while条件不成立的时候执行
    print("这里是else")
