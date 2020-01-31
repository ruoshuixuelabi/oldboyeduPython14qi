def add(a, b):
    return a + b
def test():
    for i in range(4):
        yield i
g = test()