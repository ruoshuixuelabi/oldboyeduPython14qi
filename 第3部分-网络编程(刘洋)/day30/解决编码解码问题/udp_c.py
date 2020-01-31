from My_UDP import MySocket

sk = MySocket()

sk.my_sendto('abcabc中国',('127.0.0.1',8080))


sk.close()

