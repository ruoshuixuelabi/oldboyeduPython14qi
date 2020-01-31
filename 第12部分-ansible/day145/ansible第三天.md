#  上周回顾

host-pattern格式

- 单个主机
- 多个主机,逗号隔开
- 全部主机,all
- 单个组
- 多个组
  - 交集 'web:&db'
  - 并集
    - 'web,db'
    - 'web:db'
  - 差集 'web:!db'
- 命令相关模块
  - command  不支持特殊字符<>!;|$
  - shell
  - script 执行管控机上的文件(shell\python\ruby\perl)
- 文件相关模块
  - copy
  - file   在管控机上创建文件,文件夹,软连接,硬链接
  - fetch 拉取被管控机上的文件到管控机,每个被管控机都会创建一个文件夹,并保持原来的目录结构
- 软件相关模块
  - yum
  - pip
  - service
- 用户相关模块
  - user
  - group
- 计划任务
  - cron
- playbook
  - yaml
  - 正常的格式
  - 传参
    - -e
    - hosts文件
    - playbook
    - hosts文件[groupname:vars]
    - register
    - -e > playbook > hosts
  - 条件判断
    - when
  - 标签
    - tags
  - 模板
    - template
  - 循环
    - with_items
  - handlers

# 今日内容

## roles

特点

- 目录结构清晰
- 重复调用相同的任务

目录结构

```shell
web
- tasks
  - install.yml
  - copyfile.yml
  - start.yml
  - main.yml
- tempaltes
  - nginx.conf.j2
- vars
  - main.yml
- files
- handlers
  - main.yml
```

​      tasks目录里面的查找规则: 先找main.yml,通过import_tasks来导入task, notify去找handlers里面的main.yml里面的task,tmplate模块去templates目录里面找需要复制的文件



​     



# openpyxl

xlrd\xlwt 操作excel2003之前的版本

openpyxl操作excel2003之后的版本







# 今日内容总结

ansible roles

roles

- web
  - tasks
    - main.yml
  - templates
    - j2文件
  - files
  - vars
    - main.yml
  - handlers
    - main.yml
- openpyxl
  - 写
    - wb['B2']
    - wb.cell(row=2,column=4,value='value')
  - 读
    - load_weekbook
    - wb['B2'].value
    - wb.cell(row=2,column=4').value
    - max_row
    - max_column
  - 







横向扩展(加配置)

纵向扩展(加机器)





去IOE运动

I IBM的小型机     pc 服务器 dell

O oracle数据库   mysql

E EmC的存储      自己搭建





微服务

rpc

