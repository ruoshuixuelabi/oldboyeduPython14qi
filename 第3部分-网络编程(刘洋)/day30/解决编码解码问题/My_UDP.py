
import socket


class MySocket(socket.socket):# 继承自 socket文件中的socket类,此时socket就是父类
    def __init__(self,encoding='utf-8'):
        self.encoding = encoding
        super(MySocket, self).__init__(type=socket.SOCK_DGRAM)#  执行父类socket中的__init__方法

    def my_sendto(self,msg,addr):
        return self.sendto(msg.encode(self.encoding),addr)# 调用父类中的sendto方法

    def my_recvfrom(self,num):
        msg_r,addr = self.recvfrom(num)# 调用父类的recvfrom方法
        return msg_r.decode(self.encoding),addr

