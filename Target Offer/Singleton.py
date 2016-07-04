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
print(one == two)
print(one is two)

'''
方法1的升级版, 使用__metaclass__元类的高级python用法
'''
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance

class Myclass2(object):
    __metaclass__ = Singleton2
    a = 1

one = Myclass2()
two = Myclass2()

print(id(one))
print(id(two))
print(one == two)
print(one is two)