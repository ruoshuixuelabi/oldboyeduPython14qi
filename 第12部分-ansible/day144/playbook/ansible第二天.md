# 今日内容回顾

ansible 安装 epel源

host-pattern的格式

-  单台机器
- 多台机器
- 全部机器
- 单个分组
- 多个分组
  - 交集 'web:&db'
  - 并集 
    - 'web:db'
    - web,db
  - 差集 'web:!db'
- 命令相关
  - command 不支持特殊字符<>|!;$
  - shell
  - script
- 文件相关
  - copy
    - dest
    - src
    - group
    - owner
    - mode
    - backup
    - content
  - file
    - path
    - src
      - link
      - hard
    - state
      - directory
      - file
      - touch
      - link
      - hard
    - group
    - mode
    - owner

# 今日内容详解

### fetch

用来拉取 被控机上的文件,每个被控机都会创建一个文件夹,并且保留原来的目录格式

```shell
ansible web -m fetch -a 'dest=/tmp src=/var/log/cron'
```

## 软件包相关

### yum

- rpm 与yum的 区别

  - redhat package manage

- yum源配置方式

  ```shell
  [epel] # 组名
  name=Extra Packages for Enterprise Linux 7 - $basearch #名称
  baseurl=http://mirrors.aliyun.com/epel/7/$basearch #url,可以写http,https,ftp,file:
  failovermethod=priority
  enabled=1 #是否启用 1表示启用,0表示不启用
  gpgcheck=0 #是否校验gpgcheck,0表示不校验,1表示校验
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
  ```

- yum 安装包组

  ```shell
  yum grouplist 查询包组
  yum groupinstall -y 'Development Tools' 安装包组
  rpm -qa |grep python2-pip 查看软件包是否安装成功
  ```

  ```shell
  ansible web -m yum -a 'name=python2-pip' 安装python2-pip包
  ansible web -m yum -a 'name=@Development Tools' 安装python2-pip包
  ```

## pip

```shell
pip freeze > a.txt 给当前python环境的包打快照
pip install -r a.txt 安装文件里面所有的包
pip list 查看所有安装的包
```

```shell
ansible web -m pip -a 'name=flask' 安装pip包
```

### service

```shell
service nginx start|stop|restart # centos6
chkconfig add nginx 
chkconfig nginx on 设置开机自启动
chkconfig --list
systemctl start nginx # centos7
systemctl  enable nginx # 设置开机自启动
ss -tnlp
```

```shell
ansible web -m service -a 'name=nginx state=started' #启动服务
ansible web -m service -a 'name=nginx state=stopped' #停止服务
```

## 计划任务

### cron

```shell
分 时 日 月 周 job
1 0 * * *
* * * * * tar zcvf /tmp/etc.tar.gz /etc/ 这是一个错误的示范
2 */3 * * * 每个3小时
0 15-17 * * 2,3 每周2,周三,15-17点的0分做某件事
```

```shell
day:天
hour:小时
job:执行的任务
minute:分钟
month:月
name:名字
weekday:周
ansible web -m cron -a 'minute=10 job="touch /tmp/alex.txt" name=touchfile' #新建计划任务
ansible web -m cron -a 'minute=10 job="touch /tmp/alex.txt" name=touchfile disabled=yes' #关闭计划任务
ansible web -m cron -a 'name=touchfile state=absent' #删除计划任务

```

## 用户相关

```shell
用户:
超级用户 root 0
系统用户 不能登录 201-999 centos7 1-499 centos6
普通用户  可以登录系统 1000-60000 centos7 500-65535 centos6
组:
超级组 root 0
系统组 201-999 centos7 1-499 centos6
普通组 1000-60000 centos7 500-65535 centos6
useradd -d /opt/alex alex 指定用户的家目录
useradd -M -d /opt/alex3 alex3 不创建用户的家目录
userdel -r alex3 删除用户并删除用户的家目录
```

用户和组的关系

- 一对一 主组
- 一对多 附加组
- 多对多

```shell
ansible db -m user -a 'name=mysql home=/opt/mysql groups=root uid=2000' #创建用户,并指定用户的家目录 ,指定用户的附加组,指定用户的uid
ansible db -m user -a 'name=mysql state=absent' #删除用户但是不删除用户的家目录
ansible db -m user -a 'name=mysql state=absent remove=yes' #删除用户并删除用户的家目录
```

### group

```shell
ansible db -m group -a 'name=wusir' 创建一个普通组
ansible db -m group -a 'name=wusir state=absent' 删除组
```

### setup

```shell
ansible_all_ipv4_addresses 所有的ipv4地址
ansible_all_ipv6_addresses 所有的ipv6地址
ansible_architecture 系统的架构
ansible_date_time 系统时间
ansible_default_ipv4 系统的默认ipv4地址
ansible_distribution 系统名称
ansible_distribution_file_variety 系统的家族
ansible_distribution_major_version 系统的版本
ansible_domain 系统所在的域
ansible_fqdn 系统的主机名
ansible_hostname 系统的主机名,简写
ansible_os_family 系统的家族
ansible_processor_cores cpu的核数
ansible_processor_count cpu的颗数
ansible_processor_vcpus cpu的个数

```



web

- 创建一个用户alex   ansible web -m user -a 'name=alex'
- 创建一个用户组wusir ansible web -m group -a 'name=wusir'
- 复制/etc/fstab文件到/tmp目录下面  ansible web -m copy -a 'dest=/tmp/fstab src=/etc/fstab'
- 安装nginx  ansible web -m yum -a 'name=nginx'
- 安装redis   ansible web -m yum -a 'name=redis'
- 并新建crontab每天的晚上12点重启nginx  ansible web -m cron -a 'minute=0 hour=0 job=重启'

 ## playbook

### yaml

```shell
列表: -
字典: key:value
后缀名:yaml yml
```

### ansible-playbook的命令格式

```shell
ansible-playbook [options] playbook.yml [playbook2 ...]
-C --check 干跑 白跑
-f FORKS 用来做并发的
--list-hosts 列出主机列表
--syntax-check 语法检查
-e 传递参数
-t 指定tags
```

单台机器

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: createuser
    user: name=alex
  - name: creategroup
    group: name=wusir
  - name: installredis
    yum: name=redis
```

多台机器

```shell
- hosts: web
  remote_user: root
  tasks:
  - name: createuser
    user: name=wengang
  - name: creategroup
    group: name=gebixiaoguniang
    执行过程,所有机器都执行完第一个任务,在去执行第二个任务
```

### playbook的参数

```shell
- hosts: web
  remote_user: root
  tasks:
  -  name: create{{ user }}
     user: name={{ user }}
```

第一种传参方式: -e

第二种传参方式:hosts文件里面主机后面写

第三种传参方式:hosts文件里面写[groupname:vars]

第四种传参方式:playbook文件中vars来指定

```shell
- hosts: web
  remote_user: root
  vars:
  - user: alexsb5
  tasks:
  -  name: create{{ user }}
     user: name={{ user }}
```

第五种传参方式:通过register注册,使用的时候要使用参数的.stdout值

```shell
- hosts: web
  remote_user: root
  tasks:
  -  name: sum
     shell: echo 2+4|bc
     register: user 
  -  name: create{{ user }}
     user: name=alexsb{{ user.stdout }}
```



```shell
-e > playbooks的vars > hosts文件
```

### 条件判断

```shell
- hosts: cache
  remote_user: 文刚
  tasks:
  - name: 偷看姑娘
    dong: 偷看姑娘
    when: 站着
  - name: 偷看姑娘
    dong: 偷看姑娘
    when: 趴着
```

```shell
- hosts: web
  tasks:
  - name: file
    copy: content="凿壁偷光" dest=/tmp/wg.txt
    when: num=="2"
  - name: file
    copy: content="刷流氓" dest=/tmp/wg.txt
    when: num=="4"
```

```shell
- hosts: cache
  tasks:
  - name: createfile
    copy: content="小弦切切如私语" dest=/tmp/ppx.txt
    when: ansible_processor_vcpus==1
```

```shell
- hosts: cache
  tasks:
  - name: createfile
    copy: content="小弦切切如私语" dest=/tmp/ppx.txt
    when: ansible_python.version.major==1 #取字典内的值
```

### 标签

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: install
    yum: name=redis
  - name: copyfile
    copy: dest=/etc/redis.conf src=/root/redis.conf
  - name: startredis
    service: name=redis state=started
```

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: install
    yum: name=redis
    tags: install
  - name: copyfile
    copy: dest=/etc/redis.conf src=/root/yaml/redis.conf
    tags: copyfile
  - name: startredis
    service: name=redis state=started
    tags: start
```

### 模板

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: install
    yum: name=redis
    tags: install
  - name: copyfile
    template: dest=/etc/redis.conf src=redis.conf.j2 # 可以使用相对路径,在当前目录的templates目录里面
    tags: copyfile
  - name: startredis
    service: name=redis state=started
    tags: start
```

### 循环 with_item

```shell
- hosts: web
  remote_user: 文刚
  tasks:
  - name: 偷看姑娘A
    dong: 偷看姑娘A
  - name: 偷看姑娘B
    dong: 偷看姑娘B
  - name: 偷看姑娘C
    dong: 偷看姑娘C
```

进阶版

```shell
- hosts: web
  remote_user: 文刚
  tasks:
  - name: 偷看姑娘A
    dong: 偷看{{item}}
    with_items:
    - 姑娘A
    - 姑娘B
    - 姑娘C
```

```shell
- hosts: db
  tasks:
  - name: creatuser
    user: name={{ item }}
    with_items:
    - alex10
    - wusir10
    - taibai10
```

### 循环嵌套

```shell
- hosts: db
  tasks:
  - name: group
    group: name={{item}}
    with_items:
    -  alex20
    -  wusir20
    -  taibai20
  - name: creatuser
    user: name={{ item.name }} group={{item.group}}
    with_items:
    - {name: alex30,group: alex20}
    - {name: wusir30,group: wusir20}
    - {name: taibai30,group: taibai20}
```

### handlers

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: install
    yum: name=redis
    tags: install
  - name: copyfile
    template: dest=/etc/redis.conf src=redis.conf.j2
    tags: copyfile
    notify: restart redis
  - name: startredis
    service: name=redis state=started
    tags: start
  handlers:
  - name: restart redis
    service: name=redis state=restarted
```



# 今日内容总结:

- fetch

  - 每台机器都有一个文件夹,并且保持原来的目录的结构

- yum

  - name=@development tools 安装包组

- pip 

- service

- cron

  - disabled=yes
  - 分钟最好不要是*

- user

  - remove=yes

- group

- playbook

  - 基本
  - 传参
    - -e
    - hosts文件ip地址后面
    - hosts文件[gorup:vars]
    - playbook里面vars
    - register
    - -e > playbook > hosts
  - when
  - with_items
  - handlers
    - notify
  - template
  - 标签 -t

  



