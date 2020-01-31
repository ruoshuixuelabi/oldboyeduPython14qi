
#print(1+3)
#print((1+3)*2)
#print((((1+3)*2)-6)*3)
# 注释. 对程序的标注. 给人的看的
# 变量: 变量是程序运行过程中产生的中间值. 暂时存储在内存中. 供后面的程序使用
# 变量直接声明就可以了
# #表示单行注释
# 多行注释(文档注释) 
# a = 1+3	# 把1+3的结果赋值给前面的变量a
# print(a)

''' 
	多行注释
	print(b)
	alex就是一个大xx. 我没说
	wusir也是
	太白. 也是.
	光头

 
 
	变量的命名规则:
	1. 必须使用英文字母, 数字, 下划线组成.
	2. 不能是数字开头, 更不能是纯数字
	3. 要有意义
	4. 不要太长
	5. 不要用中文
	6. 禁止用关键字,
	7. 区分大小写
	8. 推荐使用两种形式:
		1. 驼峰. 除了第一个字母外的其他单词的首字母大写. 其他小写
		ageOfAlex
		2. 下划线. 每个单词用下滑线分开
		wife_of_wusir_is_not_a_good_girl
	

 
__ = "alex"
_a_b_1 = "wusir"
1_2_a_b = ""
print(1_2_a_b)

a = 10
b = 20


a = 10
b = 20

b = a	# b = 10 , a= 10

a = 30	# a = 30 b = 10

print(a)	# 10
print(b)	# 10


a = 10
print(a) 
print("a")	# a 有坑

python不存在绝对的常量. 一般, 所有字母大写. 常量


PI = 3.141592653589793626
PI = 3.5	# 尽量不要改
print(PI)


a = 128
print(type(a))	# 打印变量a的数据类型  a 是int类型


# 字符串
s = "我叫周润发"
print(type(s))


s = '我也叫渣渣会'
print(s)


s = """我家大门常打开
我家的狗总丢
谁拉走吃肉了
还给我一个腿就行了
"""
print(s)
print(type(s))


# 请你打印出: 周杰伦说:"昆凌也还不错. 我很欣慰!"
# print('周杰伦说:"昆凌也还不错. 我很欣慰!"')

print("你好", end="")	# 在print之后. python解释器会自动的添加换行符
print("何泽伟", end="")
print("大阳哥", end="")

print("你好", "大阳哥", "何泽伟")



a = 10
print("a = ", a)	# a =  10



s1 = "sylar"
s2 = "wusir"
s3 = "alex"

s4 = s1 + s2 + s3	# 字符串拼接(连接)
print(s4)

print("我们村有个大姑娘叫"+s3+",娶了我们村更漂浪的大姑娘:"+s2)	# 


s = "考试\n"	

print(s*3)	# s 重复 3次



b = 2 > 1	# bool类型的数据只有两个取值. True, False
print(b)
print(type(b))	# 布尔类型



# print("刘德华没有我帅")

s = input("刘德华有没有我帅?")	# 获取用户输入的内容, 接收的内容永远是字符串
print("计算机收到的内容是:", s)
print(type(s))

'''
a = input("请输入一个数:")
a = int(a)	# 把传进去的内容转换成数字
b = input("请输入另一个数:")
b = int(b)
print(a+b)	# a, b都是int类型



