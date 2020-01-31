from My_UDP import MySocket

sk = MySocket()

sk.bind(('127.0.0.1',8080))

msg,addr = sk.my_recvfrom(1024)


print(msg)

sk.close()
