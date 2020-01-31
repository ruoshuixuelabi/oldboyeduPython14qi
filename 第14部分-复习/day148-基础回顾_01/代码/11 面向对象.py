"""
    面向对象:
        啥是对象: 一切都是对象
        抽象->最难->设计模式
        单例, 工厂, 门面, 适配器, 代理模式, 模板模式
        
        对象是通过类创建的
        class 类名:
            country = "大清" # 类变量. 属于类
            def  __init__(self, xxx):
                self.xxx = xxx 设置属性 实例变量, 属于对象
                
            def method(self): # 实例方法, 必须用对象去访问
                pass
            
            @classmethod
            def classmethod(cls):  类方法, 类方法属于类.
                pass
                
            @staticmethod
            def staticmethod():
                pass
                
            @property # 把方法伪装成属性
            def age(self):
                return 10
                
            @age.setter
            def age(self, x):
                self.age = x
                
            私有
            def __tou(self):
                pass
                
        实例化对象
           变量/引用 = 类名()
           对象.属性  => 访问属性信息
           对象.方法 => 访问类方法, 实例方法
           
        
        类与类之间的关系
            1. 依赖关系
                通过参数把另一个类的对象传递进来. 使用一下.
                类与类之间的关系不紧密
                解耦
            2. 关联关系, 组合关系, 聚合关系
                类与类之间的关系很紧密. 一个挂, 可能都要挂
                self.boy = peron("周杰伦")
            3. 继承和实现
                继承可以节省代码
        
        面向对象三大特征:
            1. 封装
                封装属性
                封装方法
            2. 继承
                子类可以自动的拥有父类中除了私有内容外的其他所有内容
                class 类(父类):
                    def fu():
                        super().fu()
                        pass
            3. 多态
                鸭子模型-->只要会嘎嘎叫就是鸭子
                同一个对象多种形态. 多态性
                
               
        反射
            hasattr
            getattr
            
            setattr
            delattr
            
        __init__
        __new__
        __call__   callable()
        __getitem__    对象[]
        __setitem__    对象[]  = 值
        __enter__  with 类() as 对象:进
        __exit__   with 类() as 对象:出
        
        __hash__  可以控制是否可哈希
        __eq__     == 判断
        __len__    len()
        __repr__   repr()
        __str__    str()
        __iter__   for循环
        __dict__   把属性装字典
        __mro__    方法的搜索顺序 py3用的是C3算法
        __add__    + 调用
        
        
    面向过程:
        核心是过程.

"""
# class School:
#     def __init__(self, g):
#         self.teacher_list = []
#
# class Teacher:
#     pass

# Spring:
#     Spring Boot
#     Spring Cloud
#     Spring Data
#     Spring JPA
# Struts: MVC
# Hibernate: 数据库操作
# Mybatis: 数据库操作

#
# class Girl:
#     pass
#
# g = Girl()
# b = Boy(g)
#
# print(b.g.name)

#
# class PersonFactory:
#     @staticmethod
#     def getPersonInstance():
#         return Person2()
#
#
# p = Person2()
# p = Person2()
# p = Person2()
# p = Person2()
# p = Person2()
# p = Person2()
# p = Person2()
# p = Person2()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()
# p = PersonFactory.getPersonInstance()


# class Person:
#     country = "大清"  # 类变量. 属于类
#     @property
#     def age(self):
#         return 1
#
#     @age.setter
#     def age(self, x):
#         print(x)
#
# p = Person()
# print(p.age)
# p.age = 18


#
# p1 = Person()
# p2 = Person()
# p1.country = "民国" # 对象.属性 = 值. 会给这个对象添加一个新属性
# Person.country = "民国"
#
# print(p2.country)
#
# def jiao(duck): # 要鸭子
#     duck.gagagajiao() # 嘎嘎叫
#
# class Duck:
#     def gagagajiao(self):
#         print("嘎嘎嘎嘎嘎叫")
#
# class Monkey:
#     def gagagajiao(self):
#         print("嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎叫")
#
#
# m = Monkey()
#
# jiao(Monkey())

class Person:
    __hash__ = None
    

p = Person()
print(hash(p))
