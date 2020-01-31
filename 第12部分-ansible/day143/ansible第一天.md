# 自我介绍

王胜辉

# 目的

系统:代码发布系统



# 前戏:

ansible

openpyxl



puppet

ansible

saltstack



# ansible

批量在远程主机上执行命令

python2.7编写

## 安装

第一步:下载epel源

```shell
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
```

第二步:安装

```shell
yum install -y ansible
```

## ansible 命令格式

```shell
Usage: ansible <host-pattern> [options]
-a MODULE_ARGS 模块参数
-C, --check  检查语法
-f FORKS 并发
--list-hosts 列出主机列表
-m MODULE_NAME 模块名字
```

ssh 认证方式

- 密码
- 秘钥
  - ssh-keygen 生成密钥对
  - ssh-copy-id 复制公钥到远程主机
  - 私钥加密,公钥解密

  查看ansible生成的文件

```shell
rpm -ql ansible
/etc/ansible
/etc/ansible/ansible.cfg  # ansible 配置文件
/etc/ansible/hosts
/etc/ansible/roles
```

## ping 走的是ICMP协议

## ansible第一条命令

```shell
ansible 192.168.12.26 -m ping  ping 一台机器
ansible 192.168.12.26,192.168.12.28 -m ping ping多台机器
ansible all -m ping ping所有机器
ansible web -m ping ping 一个组
ansible 'web:!db' -m ping ping web中有但是db中没有
ansible "web:&db" -m ping ping web和db的并集
ansible "web:db" -m ping  ping web和db的交集

```

hosts文件内容

```shell
# It should live in /etc/ansible/hosts
#
#   - Comments begin with the '#' character #是注释
#   - Blank lines are ignored 空行被忽略
#   - Groups of hosts are delimited by [header] elements []表示主机组
#   - You can enter hostnames or ip addresses  可以输入主机名或者ip地址
#   - A hostname/ip can be a member of multiple groups 一台主机可以被分配多个组
 www[001:006].example.com www001到www006.example.com
```

### host-pattern格式

- 单个的机器
- 多个的机器,逗号隔开
- 全部机器,all
- 可以写一个分组
- 可以写多个分组
  - 并集
    - 逗号隔开
    - 冒号隔开
  - 交集,:&隔开
  - 差集: :!隔开

## ansible-doc 查看模块帮助信息

```shell
 ansible-doc [-l|-F|-s] [options] [-t <plugin type> ] [plugin]
 -j 以json格式显示所有模块信息
 -l 列出所有的模块
 -s 显示模块的摘要信息
 # 直接显示模块的所有帮助信息

```

ansible 特性: 幂等性 不管执行几次,结果都是一样的

# 命令相关

## command

```shell
ansible web -a 'ls'
ansible web -a 'chdir=/tmp pwd'  # 先切换目录,在执行相应的命令,一般情况下在编译时候使用
ansible web -a 'creates=/tmp pwd' # 如果creates的文件存在,则不执行后面的操作
ansible web -a 'removes=/tmp pwd' # 如果removes的文件存在,则执行后面的操作
ansible web -a 'removes=/tmp mkdir /data' # 会执行后面的mkdir命令
ansible web -a 'creates=/data2 mkdir /data2' #会执行后面的mkdir命令

```

补充

```shell
查看用户是否被创建成功
tail -1 /etc/passwd
tail -1 /etc/shadow
id
echo '1' | passwd --stdin alex 非交互式设置密码
```

## shell 

```shell
<>|;& $ 这些特殊字符command不支持
ansible web -m shell -a 'echo "1" | passwd --stdin alex' 设置alex的密码
ansible 192.168.12.25 -m shell -a '/root/a.sh' 执行shell脚本,前提是脚本有可执行权限
ansible 192.168.12.25 -m shell -a '/root/a.py' 执行python脚本,前提是脚本有可执行权限

```

## script

```shell
ansible db -m script -a '/root/m.sh' 执行管控机上的文件
ansible web -m script -a 'creates=/root/a.sh /root/m.sh' # 查看的是被管控机上的文件是否存在
```

# 文件相关的模块

## copy

```shell
 ansible db -m copy -a "dest=/tmp/a.sh src=/root/m.sh" 复制文件到远程主机
 ansible db -m copy -a "dest=/tmp/a.sh src=/root/m.sh backup=yes" 复制文件并备份远程文件
 ansible web -m copy -a "dest=/tmp/a.sh src=/root/m.sh owner=alex mode=700" 修改复制后的文件的属主和权限
 ansible web -m copy -a "src=/etc/init.d dest=/tmp" 复制目录到远程主机
 ansible web -m copy -a "src=/etc/init.d/ dest=/tmp" 复制目录里面的文件到远程主机
 ansible web -m copy -a "src=/etc/ansible dest=/tmp owner=alex" 复制目录到远程主机,并修改目录的属主,并且里面文件的属主也被修改了
 ansible web -m copy -a "content='大弦嘈嘈如急雨,小弦切切如私语' dest=/tmp/b.txt"  直接将content里面的内容添加到dest的文件里面
```

## file 

### 补充

```shell\
ln -s 原文件地址 目标文件地址   创建软连接
ln 创建硬链接
```

```shell
ansible cache -m file -a "path=/tmp/wupeiqi  state=directory" 创建一个目录
ansible cache -m file -a "path=/tmp/wupeiqi.txt  state=touch" 创建一个文件
ansible cache -m file -a "path=/tmp/t  state=link src=/etc/init.d" 创建软连接 path是目标文件 src是源文件
ansible cache -m file -a "path=/tmp/t  state=absent " 删除文件
```

## 今日内容总结

```shell
ansible 安装 epel源

```

host-pattern格式

- 单个主机
- 多个主机
- all
- 一个组
- 多个组
  - 交集 'web:&db'
  - 并集 'web:db'
  - 差集 'web:!db'

命令相关的模块

- command 不支持特殊字符  <>;!$|&
- shell
- script 执行管控机上的脚本

文件相关的模块

- copy 

  - content
  - dest
  - src
  - onwer
  - group
  - mode
  - backup

- file

  - path
  - state
    - directory
    - touch
    - file
    - absent
    - link
    - hard
  - src
    - link
    - hard

  