# 第三部分串讲 2019-02-27

## 前端

### HTML

标签

块儿级标签

行内标签

form表单提交 三要素:

1. action:往哪里提交数据(为空表示往当前URL提交)
2. method: GET/POST
3. name属性:获取用户输入的标签都需要有name属性
4. submit提交按钮: 默认有提交form表单的动作

HTML属性:

​	style

​	id

​	class

​	name

​	value

​	option

​	title

​	src

​	...

### CSS

### CSS选择器

* ID选择器:唯一找标签
* 元素选择器:固定找某个标签
* 类选择器: 给不同的标签设置相同的样式
* 组合选择器: 
  * 后代   `p a`
  * 毗邻  `p+a` `label+input`
  * 儿子  `p>a`
  * 弟弟  `p~a`
* 属性选择器  `p[name='kangchen']`
* 分组选择器  `a,p{color:red}`
* 通用选择器  `*{margin:0}`
* 伪类

**选择器的优先级**

内联(1000) > ID选择器(100) > 类选择器(10)>元素选择器(1)>继承



### CSS属性

文本样式

字体

背景

边框

浮动

CSS盒子模型	

​	content->padding->border->margin

宽度高度

overflow

display

定位

​	绝对定位

​	相对定位

​	固定定位

z-index

opacity

### JS

#### 语法基础

数据类型: String number boolean object undefined null 

运算符

​	强等于 `===`

流程控制语句

​	switch

​	三元运算

函数

​	作用域

1. 普通函数
2. 匿名函数  箭头函数
3. 自执行函数`(function(){})()`

内置的对象

​	Date

​	Math

​	RegExp

​	JSON

作用域

### BOM&DOM

定时器

查找标签:

```javascript
document.getElementById('b1')
document.getElementsByClassName('c1')
document.getElementsByTagName('p')
```

操作标签

操作文档

### 事件

常用事件

事件的绑定方式

事件冒泡与阻止冒泡

事件委托:基于一个已经存在的元素给未来的元素绑定事件mmmmmmmmmmmmmmmm

### jQuery

jQuery中文文档

#### 选择器和筛选器

#### 文本操作/文档操作/属性操作

#### 事件

#### 动画

####  插件\ each循环 \data\AJAX 

### Bootstrap

1. 栅格系统
2. 常用CSS样式
3. 内置的组件 
   1. 图标(font-awosome\icon-font)
   2. 面板
   3. 导航条
   4. 进度条
   5. 输入框组
   6. 按钮
4. JS插件 
   1. 轮播图
   2. 模态框
   3. sweetalert

## Vue

### ES6

1. let和const
2. 模板字符串 `${n}`
3. 面向对象
4. 箭头函数
5. 对象深拷贝
6. Promise 了解

### Vue指令

Vue介绍: 渐进式的单页面数据驱动视图框架

v-if

v-for

v-model

v-on

v-bind

v-show

v-text

小清单示例



### Vue组件

局部组件



全局组件

```vue
Vue.component('组件名', {template:"", data(){return {}}})
```



父组件->子组件传值

父组件 v-on:name="kangchen"

子组件: `props:['name']`

子组件->父组件传值

子组件抛出自定义事件:`this.$emit('事件名', '数据')`

父组件监听 自定义事件:`v-on:事件名=函数`

非父子组件间传值

借助中间对象

var bus = new Vue()

组件1: `bus.$emit('事件名',数据)`

组件2: `bus.$on('事件名')`

### Vue生命周期

Hook 钩子函数

### Vue Router 

`$route` :当前路由信息

`$route.params`

`$router`:全局路由对象

前端路由

`router-link`

`router-view`

嵌套的路由

路由的参数

命名路由

编程式导航

### 前端开发工具

1. node.js : 解释器 让JS可以运行在服务器上
2. npm: 包管理工具
3. webpack:前端开发打包工具 用后端开发的方式开发前端代码
4. Vue-CLI:搭建Vue项目的脚手架工具

### VueX

大型项目用到的状态管理器(管理跨组件的一些数据)

action:异步操作(ajax请求)

mutation:同步操作(赋值)

commit:

### axios

Vue推荐的发送请求的工具

### Element-UI

类似Bootstrap

Vue全家桶:Vue VueRouter  VueX

## Django

### Django基础

MTV架构

Django请求的生命周期  

![1551252533252](E:\PythonS14\第三部分串讲\assets\1551252533252.png)

WSGI 

WEB框架本质

通过socket收发消息, 浏览器是客户端,后端python是服务端

对HTML文件做字符串替换

### ORM  

​	ORM字段参数

​		如何实现MySQL中`char`类型的字段  --> 自定义字段类型

​	ORM单表查询 -- 必知必会13条

1. 返回QuerySet对象
   1. all
   2. filter
   3. exclude
   4. order_by
   5. reverse
   6. distinct
   7. values
   8. values_list
2. 返回对象
   1. get
   2. first
   3. last
3. 返回数字
   1. count
4. 返回布尔值
   1. exists

​	ORM连表查询 -- 正向查询和反向查询

​	神奇的双下划线

​	多对多的关系的三种方式

​	[聚合和分组](https://www.cnblogs.com/liwenzhou/p/8660826.html)

​	F查询和Q查询

​	事务

```python
    from django.db import transaction
    with transaction.atomic():
        #  事务操作
```

​	ORM行级锁

​	`select_for_update()`

​	执行原声SQL语句的方式

​	`.extra()`

​	`.raw()`

​	性能优化

​		`bulk_create`

​		`select_related`/`prefetch_related`

​	如何在单独的脚本里面执行ORM操作

​	only和defer 

路由

​	二级路由 `namespace`

​	命名路由 `name`

​	反向解析路由

​	分组匹配和分组命名(不能同时用)  --> 将捕获的值传递给了视图函数

### 模板

​	模板的变量语法 

​	模板逻辑语法

​	filter  对变量做操作的   `{{变量|filter名}}`

​	simple_tag :可以 传入多个参数 返回一个结果

​	inclusion_tag :将数据渲染到一段HTML代码中返回

母板和继承

组件/块

静态文件相关

`mark_safe`

### 视图

​	request对象

​		request.GET

​		request.POST

​		request.FILES

​		request.methods

​		request.META

​		request.body

​		request.parth_info

​		request.get_full_path()

​		request.session

​		request.user

​	response对象

​	FBV和CBV

​	CBV加装饰器

​		`csrf_excspt`

​		`csrf_protect`

​		`method_decorator`

掌阅面试:[类装饰器](https://www.liwenzhou.com/posts/Python/advanced_decorator/)



### Django进阶

Cookie和Session

为了弥补HTTP无状态,引申出来的一个概念

Token认证 、JWT（重要）



中间件

​	**五个方法**

​	`process_request`

​	`process_view`

​	`process_template_response`  仅当视图函数返回一个带render方法的对象时才会执行

​	`process_exception` 仅当视图中抛出异常的时候会执行

​	`process_response`

​	**四个要点**

​	执行时间点

​	执行顺序

​	参数

​	返回值

Form模块及Modelform\formset

1. 生成HTML form表单
2. 校验数据有效性并保存之前输入的内容
3. 返回错误提示

Modelform：把model类和数据绑定

`.save()`

modelformset:批量创建form表单

#### auth模块

认证的原理

认证的内置方法

自定制一个auth对应的user 表

 	1. 自己创建一个User表继承AbstractUser
 	2. 在settings.py中指定 AUTH_USER_MODEL='app名.User类名'



contenttypes(根据表名动态关联)

`GenericForeignKey`

`GenericRelation`

数据库设计三大范式：《漫画数据库》

[跨域](https://www.cnblogs.com/liwenzhou/p/9513648.html)

JSONP

CORS

简单请求和非简单请求

admin

分页

缓存

​	Django内置的缓存

​	自己配Redis缓存

[信号](https://www.cnblogs.com/liwenzhou/p/9745331.html)

[日志](https://www.cnblogs.com/liwenzhou/p/8763264.html)

## CRM

#### 权限系统

**理论基础**

`RBAC`：基于角色的权限控制

好处：权限的配置和管理简单。

**代码实现**

登录：强制登录（白名单：登录页面、注册页面等） --> 动态的配置做成配置项不要写死在代码中。

​		把该用户拥有的权限都加载出来（`init_permission()`）

​		存到`request.session` | 存到redis也可以

权限校验:

​	哪个时间点做校验：中间件的`process_request`

​	怎么做：

​		取到当前的访问URL

​		判断URL在不在白名单、

​		如果不在白名单：

​			判断当前的URL在不在当前用户的权限内



`面包屑导航` `二级菜单` 让大家练习数据结构和MVC开发模式

​	要实现某个需求：

​		从数据库取数据

​		构建需要的数据格式

​		展示出来

#### 业务逻辑

`CRM`：客户管理系统|经销商管理|渠道管理|销售管理|库存管理|加盟商管理

客户展示列表页面

我的客户页面

客户的增删改查   --> `modelform`   --> 设置初始值

公私户转换           --> 事务和行级锁

模糊搜索和分页   --> `QueryDict`管理URL里query参数的 并urlencode编码



写到简历上的项目：一张纸一支笔一个项目说半小时

​	画项目架构图

​	项目背景

​	项目人员分配（你做什么）

​	我都用到了那些技术、知识点

​	项目的重难点（亮点）以及我的解决方法（思路） --> 说别人不容易知道的 说你成长最大的

​	项目总结：通过这个项目我换的了哪些提升

亮点：权限粒度细分到按钮、事务和行级锁防止竞争、多维度的检索条件

优化的逻辑：

​	权限的缓存由`request.session`移到`redis`

​	`Django_debug_toolbar`:SQL语句的执行时间 ORM查询优化：`select_related` 、`prefetch_related` 、`only`、`defer`

`request.session` 的原理：

​	`from django.contrib.sessions.middleware import SessionMiddleware`

​	`from django.contrib.sessions.backends import db`

​	request.session是个对象

​	request.session.get('k1') 



编辑权限后如何让权限立即生效：

​	手动修改request.session里面的记载权限数据

​	根据用户找session_key， 去`django_session`表中找session_data，修改session_data

​	用`redis`存更简单一点

​	

​	websocket



批量权限管理：

​	如何获取当前Django项目中的所有URL，脚本分析`urlpatterns`

​	集合的操作：求差集，求交集，求并集（集合可以直接加减）

![1551320568494](E:\PythonS14\第三部分串讲\assets\1551320568494.png)

​	`modelformset `

​		`{{ formset_obj.management_form }}`  告诉后端我这个formset都有多少条数据

​	formset就是多个form的集合，实现一次更新多条数据。

## DRF

`DRF`:Django REST frameowrk

RESTful：只要一套API符合REST规范，那么这套接口就是RESTful风格API

REST规范：

​	GET:获取

​	POST:创建

​	PUT/PATCH:更新

​	DELETE:删除

DRF模块：

1. 序列化：Serializer和ModelSerializer

   1. ORM对象 --> json格式数据
   2. json  --> ORM对象
   3. 数据有效性校验
   4. 字段`MethodField`、`get_xx_display()` 、`source=obj.xx`、`read_only=True`、`write_only=true`

2. 视图

   对面向对象（Python中类的使用）理解更深刻了。

   混合类：

   ​	不能单独实例化，必须配合别的类使用

   ![img](E:\PythonS14\第三部分串讲\assets\867021-20190113231720487-805070869.png)

3. 认证

   自定义认证必须实现`authentication`方法，认证通过返回元祖

   request.user, token = ()

4. 权限

   表明 某个用户是否能访问某个URL

   必须实现 `has_permission`方法，返回True就表示有权限

5. 频率

   表明某个用户一段时间内的访问次数

   必须实现`throttle`方法和`wait`方法,

   循环访问历史的列表的时候为什么要用`while`循环？

   不能在遍历一个列表等容器类元素的同时修改它的长度。

6. 分页

   分页的三种方式：页码的，基于offset，基于加密的游标

7. 版本

   域名中加版本， 请求头中加版本，url参数加版本

8. 过滤器

   在`get_queryset()`中可以对数据做过滤

9. 解析器

10. 渲染器

跨域请求：`pip install django-cors-headers`

[娜扎翻译的DRF文档](https://q1mi.github.io/Django-REST-framework-documentation/)

## 路飞

详见村长分享。



## Django写单元测试 `unittest`

单元测试

Django中单元测试



**JWT**、保利威视、CKEditor、Django如何实现读写分离





# 下午面试题：



Django中的websocket   --> `django channels`支持websocket





























