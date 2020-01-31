# 网络开发架构 C/S B/S
# 各种协议
# osi七层模型
# 应用层(表示层 会话层) http/https/snmp/pop3/stmp/ftp/dns
# 传输层  tcp/udp
    # tcp协议
        # 可靠 面向连接的全双工通信 无边界的字节流 慢 占用操作系统中的连接资源
        # 1.可靠 不是安全,更多的是保证数据的完整性
        # 2.面向连接,必须要先建立连接再进行通信 (三次握手和四次挥手)
        # 3.无边界的字节流,多条tcp数据之间是没有边界的
        # 4.慢 : 通信 建立/断开连接  保证数据完整性的机制
        # 5.占用操作系统中的连接资源(核心要解决的问题)
            # 在不使用任何异步机制(进程\线程\协程),在阻塞io模型中,一个server端只能和一个client端相连
            # 非阻塞IO模型
            # conn1,conn2,conn3
            # sk = socket.socket()
            # sk.setblocking(False)   # 异步的概念
            # conn_lst = []
            # try:
            #   conn,addr = sk.accept()
            #   conn_lst.append(conn)
            # except BlockingIOError:
            #     for conn in conn_lst :
            #         try:
            #             conn1.recv()  # 有数据在缓存里就接受,没有数据就报错
            #         except BlockingIOError:pass
            #             pass
    # udp协议
        # 不可靠 无连接 面向数据报 速度快 能够传输的数据长度有限
        # 不会粘包\速度快\可以和任意多个客户端互相通信
        # 容易丢失数据\传输的数据长度有限
# tcp协议 三次握手和四次挥手
    # 三次握手
    # 四次挥手
    # 握手:client先向server端发起SYN请求
    # 为什么挥手是4次
    
# 网络层  ipv4/ipv6 : 4位点分十进制,6位冒分16进制   icmp协议
# 数据链路层 arp协议/rarp协议  通过ip找到mac/通过mac找ip地址
    # arp涉及到的物理设备 : 二层交换机
# 物理层

# http/https 超文本传输协议
# 做什么用的 服务端和浏览器进行数据交互的
# 底层协议是什么 基于tcp协议


# 各种网络设备
# 传输层     四层防火墙\四层路由器\四层交换机
# 网络层     路由器 防火墙 三层交换机
# 数据链路层 交换机 网卡
# 物理层  网线


# 套接字 socket
# 基于TCP协议的 socket server 和client
# 扩展: 如何通过socket写一个client端来访问合同http服务

# tcp协议的粘包现象
# 明确了信息的边界,利用struct模块自定义协议来解决的问题
# 粘包现象的成因:
    # 操作系统中有一个缓存区,
    # 发送方 两条连续发出的短消息会根据tcp协议的合包机制被合在一起发送
    #       一条过长的数据也会根据tcp协议的拆包机制被分成多段数据发送
    # 接收端 所有的数据都会在接收端的缓存区中被合在一起,如果没有及时获取信息,那么消息也会黏在一起

# socketserver(threading/socket/selector)
    # 帮助你完成server端的并发效果的模块
    #
    
# socket在5层协议中在哪个位置 : 应用层和传输层直接,socket是一组封装了后四层协议数据拼接的接口

# 同步/异步(多进程/多线程/协程/IO多路复用)
# 阻塞/非阻塞
# gevent


