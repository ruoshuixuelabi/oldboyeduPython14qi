import s1

# 将任务存放在Broker
res_id_list = []
for i in range(10):
    res = s1.my_func1.delay(10, i * 10, i)
    res_id_list.append(res)

print(res_id_list)

# res = my_task.my_func1.delay(1,2)
# print(res)


# 等待执行结果的函数
# for result in res_id_list:
#     print(f"{result}执行的结果为:{result.get()}")

# 异步等待执行结果的函数
res_list = []
while len(res_list) != len(res_id_list) :
    for result in res_id_list:
        if result.successful():
            print(result,result.get())
            res_list.append(result.get())
            res_id_list.remove(result)
            break
        else:
            print(result,"还在执行中")
            
print(res_list)