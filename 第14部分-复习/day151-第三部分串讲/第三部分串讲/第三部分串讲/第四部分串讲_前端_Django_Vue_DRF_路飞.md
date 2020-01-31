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

## DRF

## 路飞



JWT\保利威视\缓存\CKEditor\日志\





