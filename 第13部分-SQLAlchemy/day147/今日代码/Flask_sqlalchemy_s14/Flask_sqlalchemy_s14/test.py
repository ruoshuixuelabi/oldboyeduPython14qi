from concurrent.futures import ProcessPoolExecutor
import time, os, random


def piao(name, n):
    print("%s is piaoing %s" % (name, os.getpid()))  # 打印了端口号
    time.sleep(random.randint(2, 3))
    return n * 2


if __name__ == "__main__":
    p = ProcessPoolExecutor(4)  # 指定进程池最大进程个数
    objs = []
    for i in range(10):
        # 这属于同步调用，要等到obj拿到结果后才会执行之后的代码
        # obj = p.submit(piao,"alex %s"%i,i).result()
        # print(obj)
        # 异步调用
        obj = p.submit(piao, "alex %s" % i, i)  # 这里只提交进程，并不拿到他们的结果,并且把进程赋值给一个变量
        objs.append(obj)  # 把进程追加进列表中
    for obj in objs:
        print(obj.result())  # 从列表中拿到进程的返回值
        # 这里提交进程时并不会遇到阻塞，进程池中的四个进程是同时运行的，一个进程运行完，就会有另一个进程开始运行
        # 在拿结果的时候可能有一个没有运行完但他后面的就运行完了，他不会跳过去取结果，会等待结果出来，这时后面的
        # 结果是计算出来的所以不用等待就能拿到结果

    p.shutdown(wait=True)
    print("哈哈哈哈")