def test():
    print('test')


def fun(fn):
    def inner():
        print('开始前')
        fn()
        print('结束后')

    return inner


# test2 = fun(test2)

# @fun   # test2 = fun(test2)
def test2():
    print('test2')


def wrapper(fn):
    def inner(*args, **kwargs):
        print('准备点钱')
        ret = fn(*args, **kwargs)  # 真正执行原来的代码
        return ret

    return inner

@wrapper   # yue = wrapper(yue)  # inner
def yue(tools):
    print('使用%s约一约' % tools)
    return '约成功了'

ret = yue('momo')

print(ret)
