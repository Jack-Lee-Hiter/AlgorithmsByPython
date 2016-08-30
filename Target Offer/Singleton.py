'''
单例模式,核心结构中只包含一个被称为单例类的特殊类,类的对象只能存在一个
三个要点: 某个类只有一个实例; 必须自行创建这个实例; 必须自行向整个系统提供这个实例
'''

'''
方法1: 实现__new__方法,然后将类的一个实例绑定到类变量_instance上
如果cls._instance为None, 说明该类没有被实例化过, new一个该类的实例,并返回
如果cls._instance不是None, 直接返回_instance
'''
class Singleton1(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton1, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class Myclass(Singleton1):
    a = 1

one = Myclass()
two = Myclass()

# one和two完全相同, 可以用id(), ==, is检测
print(id(one))
print(id(two))
print(one == two)       # True
print(one is two)       # True

two.a = 3
print(one.a)    # 3

'''
方法2：共享属性；所谓单例就是所有引用（实例、对象）拥有相同的的状态（属性）和行为（方法）
同一个类的所有实例天然拥有相同的行为（方法）
只需要保证一个类的所有实例具有相同的状态（属性）即可
所有实例共享属性的最简单方法就是__dict__属性指向（引用）同一个字典（dict）
'''
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob
class MyClass2(Borg):
    a = 1
one = MyClass2()
two = MyClass2()
two.a = 3
print(one.a)
# one 和 two 是两个不同的对象，id，==，is对比结果可以看出
print(id(one))          # 18410480
print(id(two))          # 18410512
print(one == two)       # False
print(one is two)       # False
# 但是one和two具有相同的（同一个）__dict__属性
print(id(one.__dict__)) # 14194768
print(id(two.__dict__)) # 14194768

'''
方法3：装饰器版本decorator
这是一种更pythonic，更elegant的方法
单例类本身根本不知道自己是单例的，因为他自己的代码并不是单例的
'''
def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance
@singleton
class MyClass3(object):
    a = 1
    def __init__(self, x = 0):
        self.x = x

one = MyClass3()
two = MyClass3()
two.a = 3
print(one.a)            # 3
print(id(one))          # 8842576
print(id(two))          # 8842576
print(one == two)       # True
print(one is two)       # True
one.x = 1
print(one.x)            # 1
print(two.x)            # 1

'''
方法4：import方法
python中的模块module在程序中只被加载一次，本身就是单例的
可以直接写一个模块，将你需要的方法和属性，写在模块中当做函数和模块作用域的全局变量即可，根本不需要写类。
'''
# mysingleton.py
# class My_Singleton(object):
#     def foo(self):
#         pass
# my_singleton = My_Singleton()

# to use
from mysingleton import my_singleton
my_singleton.foo()