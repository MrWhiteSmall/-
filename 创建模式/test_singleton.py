'''
单例：全局配置信息
'''

# 单例方式1
'''
def singleton(cls):
    _instance = {}
    def get_instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return get_instance

@singleton
class MyClass:
    pass

class1 = MyClass()
class2 = MyClass()

print(class1 is class2)
'''

# 单例模式2
class MyClass:
    _instance = None
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance=super(MyClass,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
class1 = MyClass()
class2 = MyClass()

print(class1 is class2)