def add(a, b):
    return a + b


def gen():
    for r_i in range(4):
         yield r_i


g = gen()

for n in [2, 10]:
    g = (add(n, i) for i in g)
print(list(g))