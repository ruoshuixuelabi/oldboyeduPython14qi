1.在登录Linux时，一个具有唯一进程ID号的shell将被调用，这个ID是什么(B)?
A.NID       B.PID        C.UID        D.CID


2.下面哪个目录存放用户密码信息（B）
A./boot        B./etc        C./var        D./dev

3.(D)不是流行的Linux操作系统。 
A.Red Hat Linux B.Mac OS C.Ubuntu Linux D.Red Flag Linux 

4.关闭linux系统（不重新启动）可使用命令 (B) 。 
A Ctrl+Alt+Del B halt C shutdown -r now D reboot 

5.用自动补全功能时，输入命令名或文件名的前1个或几个字母后按什么键？ (B) 
A.【Ctrl】键 B.【Tab】键 C.【Alt】键 D.【Esc】键 


6.在vi中退出不保存的命令是？(A) 
A. :q B. :w C. :wq D. :q! 

7.下面哪个Linux命令可以一次显示一页内容？ (C) 
A. pause B. cat C. more D. grep 

8.pwd命令功能是什么? (C ) 
A. 设置用户的口令 
B. 显示用户的口令 
C. 显示当前目录的绝对路径 
D. 查看当前目录的文件 

9.文件权限读、写、执行的三种标志符号依次是(A)。 
A rwx B xrw C rdx D srw 

10.某文件的组外成员的权限为只读；所有者有全部权限；组内的权限为读与写，则该文件的权限为( D)。 
A 467 B 674 C 476 D 764 

11.改变文件所有者的命令为 ( C)。 
A chmod B touch C chown D cat 

12.为了将当前目录下的压缩归档文件myftp.tar.gz解压缩，我们可以使用：(A)。 
A. tar -xvzf myftp.tar.gz B. tar -xvz myftp.tar.gz 
C. tar -vzf myftp.tar.gz D. tar -xvf myftp.tar.gz 

13.当运行在多用户模式下时，可以切换多少虚拟用户终端（ B ）
A、3 B、6 C、12 D、1

14.欲查询 nginx 是否有安装,可用下列那一指令（ B ）
A、rpm –ivh nginx B、rpm -q nginx
C、rpm -U nginx   D、rpm -x nginx

15.Linux 文件系统的文件都按其作用分门别类地放在相关的目录中，对于配置，一般应将其放在（ B ）目录中
A、/dev B、/ect C、/bin D、/lib

16.在linux中观看内存（物理内存、交换空间）的使用情况的命令是（ B ）
A、top B、free C、last D、lastcomm

17.观察系统当前进程的运行情况的命令是（ C ）
A、free B、dmesg C、top D、last

18. 如果执行命令 #chmod 746 file.txt，那么该文件的权限是（A）。
 A.rwxr--rw-

 B.rw-r--r—

 C.--xr--rwx

 D.rwxr--r—

19.如果您想列出当前目录以及子目录下所有扩展名为“.txt”的文件，那么您可以使用的命令是（ B）。
 A.ls *.txt

 B.find –name “.txt”

 C.ls –d .txt

 D.find . “.txt”

20.什么命令可以测试网络中本机系统是否能到达 一台远程主机 ，所以常常用于测试网络的 连通性 。  C
A.ssh
B.netstat
C.ping
D.exit

21.退出交互模式的shell，应该输入什么?	C
A. ; 
B. :q!
C. exit 
D. quit 

22.在创建文件夹时候，在其父目录不存在时候，添加的参数是？		D
A. -m
B. -d
C. -f
D. –p

23.下列文件中，包含了主机名到IP 地址的映射关系的文件是： 。	C
A. /etc/HOSTNAME
B. /etc/hosts
C. /etc/resolv.conf
D. /etc/networks

填空题
1.vi编辑器具有三种工作模式?
命令模式	编辑模式	底线命令模式

2.nginx服务器进程配置文件是?
nginx.conf

3.在 Linux系统中，压缩文件后生成后缀为.gz文件的解压命令是？
gzip -rv filename  #压缩文件为filename.gz
gzip -d filename.gz  #解压缩文件去掉.gz后缀

4.在 Linux系统中，压缩文件后生成后缀为.tar文件的解压命令是?
tar -cf filename   #压缩
tar -xf fielname.tar  #解压缩

5.在 Linux系统中，压缩文件后生成后缀为.xz文件的解压命令是？
xz -d #解压缩
xz -z  #压缩

6.WWW服务器是在Internet上使用最为广泛，它采用的是什么结构？
b/s 架构

7.nginx软件反向代理的配置参数是?
proxy_pass

8.nginx限制网站访问的配置参数是？
deny

9.如何给linux添加一个dns服务器记录
echo "nameserver 114.114.114.114" >> /etc/resolv.conf

10.每月的,5,15,25天的晚上5点50重启nginx
50 17 5,15,25 * * /usr/bin/systemctl restart nginx 


11.每周3到周5的深夜11点，备份/var/log /vmtp/
0 23 * * 3-5 /usr/bin/cp -r  /var/log/* /vmtp/

12.每天早上6.30清空/tmp/内容
30 6 * * * /usr/bin/rm -rf /tmp/* 

13.每个星期三的下午6点到8点的第5，15分钟执行命令 command
* * * * *
5,15 18-20 * * 3  commadn

14.某文件的权限为：drw-r--r--，用数值形式表示该权限，则用八进制数表示为? ，该文件属性是? 。
可读可写-可读--可读--
644

15.用来存放系统管理员使用的可执行命令目录是?
/usr/sbin/
/sbin

16.Linux的定时任务服务名是？
crontab

17.alex用户远程登录服务器123.206.16.61的命令是?
ssh alex@123.206.16.61

18.备份mysql数据库的命令是？
mysqldump -u root -p --all-databases > /tmp/db.dump
mysql -uroot -p < /tmp/db.dump


19.说说这些特殊符号含义: > >>   #(井号) .(点) ..(两个点)
>	覆盖
>>	追加
#注释
.	当前目录
.. 上级目录

20.入职新公司，老大让你在服务器上限制rm 命令，当用户输入rm 命令时候提示”rm commandis not allowed to use.” 请问实现的步骤是？
alias rm="echo rm commandis not allowed to use."

21.把test.txt 文件中的trainning 修改为oldboy的命令是？
sed -i 's/trainning/oldboy/g' test.txt

判断题
1、RedHat LINUX 安装时自动创建了根用户。 					对
2、能改变用户工作目录到根目录的命令是 cd . 					错
3、Linux 中的超级用户为root,登陆时不需要口令。 				错
4、cat filename.txt | more可实现分页地查看一个大文件的内容。  对
5、命令 echo $HOME 可以输出用户的家目录。 					对
9、RedHat Linux 使用 ls -al 命令将列出当前目录中的文件和子目录名。 		错
10、Linux系统包括虚拟终端，图形界面终端有 6 个。				错


#简答题

1.如何上传文件到Linux系统上，或从Linux上下载文件？（命令）
lrzsz	sz  rz 
xftp

2.如何查杀进程？
ps -ef
kill
pkill
killall

3.chmod如何使用？
chmod 777 filename.txt

4.如何启动和停止某项服务？
systemctl start/stop nginx

5.DNS实际上是分布在internet上的主机信息的数据库，其作用是?
解析域名	>	ip

6.Mysql在centos7上如何安装?
yum 
rpm
编译安装

7.处于安全角度，如何启动redis?
更改端口
添加密码
redis-server redis.conf	指定配置文件

8.开发环境中，你如何保证本地环境和开发环境一致性？
pip freeze > requirements.txt 

9.virtualenv是什么，如何使用？
虚拟解释器
1.创建
2.激活


10.virtualenvwrapper是什么？如何使用？
管理多个虚拟解释器
1.配置环境变量
2.workon等命令管理


11.redis哨兵是什么?
检测主从同步是否正常，可以自动分配新的主库

12.redis cluster是什么?
redis集群方案，提供了哨兵+主从功能


13.linux如何安装软件，请说出所有方式？
yum 
rpm 
源码

14.简述DNS进行域名解析的过程。
1.hosts文件
2.dns服务器

15.什么是静态资源，什么是动态资源？
图片/视频/html网页		静态资源
与数据库打交道的网页	动态资源

16.配置linux软件快捷方式的办法？有几种？怎么配置？
ln -s 目标文件 快捷方式
配置PATH

17.简述以下nginx配置的作用？

server {
        listen       80;	#端口
        server_name  192.168.11.64;	#域名或ip
        #低级匹配 nginx域名访问路径
        location / {
        	#包含语法，导入一个配置文件
             include  /opt/nginx1-12/conf/uwsgi_params;
             #nginx接收到请求，转发给uwsgi服务器
             uwsgi_pass 0.0.0.0:8000;
             root   html;	#定义网页根目录
             index  index.html index.htm;
        }
        #低级匹配，nginx域名访问路径
        #192.168.11.61/static/
　　　　  location /static{
			#alias别名参数，配置资源访问路径，只能写在location中
　　　　　　　　alias /opt/nginx1-12/static;　　　
         }

18.Linux你如何管理进程？supversior怎么用？
supervisor管理
	1.easy_install supervsor
	2.在配置文件中添加任务
	3.启动supervisor
	4.supervisorctl管理进程
19.如何发布django项目?
	nginx+uwsgi+supervisor+virtualenvwrapper

20.docker是什么?简述docker如何使用？常用命令有哪些?
	1.docker是linux容器技术
	2.安装docker，镜像，容器，仓库三大生命周期

21.备份恢复mysql
mysqldump -u root -p --all-databases > /tmp/db.dump
mysql -uroot -p < /tmp/db.dump
登录mysql，然后source /tmp/db.dump

22.redis相关
port 
requirepass
daemonize yes


