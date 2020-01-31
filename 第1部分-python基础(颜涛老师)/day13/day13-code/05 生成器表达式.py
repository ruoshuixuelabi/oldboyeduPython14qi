# g = (i for i in range(10))
# print(list(g))

# gen = ("麻花藤我第%s次爱你" % i for i in  range(10))
# for i in  gen:
#     print(i)

# 生成器的惰性机制
# def func():
#     print(111)
#     yield  222
# g = func()
# g1 = (i  for i in  g)
# g2 = (i  for i in  g1)
#
# print(list(g))
# print(list(g1))
# print(list(g2))


