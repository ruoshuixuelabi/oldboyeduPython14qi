import threading
import time
from threading import local

class Foo(object):
    pass

foo = local()
th_local = {
    6316:{foo.num:0},
    3896:{foo.num:1},
    3980:{foo.num:2}
}

def add(i):
    foo.num = i
    time.sleep(1)
    print(foo.num,i,threading.current_thread().ident)


for i in range(20):
    th = threading.Thread(target=add,args=(i,))
    th.start()