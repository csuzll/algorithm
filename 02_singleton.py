# 实现一个单例模式(最好是线程安全的)
# 基于__new__方法实现

import threading
class Singleton(object):
	# 创建一个锁
	_instance_lock = threading.Lock()

	def __init__(self):
		pass

	# cls指的是Singleton类
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "_instance"):
			# with代表自动获取和释放锁
			with cls._instance_lock:
				if not hasattr(cls, "_instance"):
					cls._instance = super().__new__(cls)
		return cls._instance


# 基于metaclass实现

"""
1.类由type创建，创建类时，type的__init__方法自动执行，
类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，
对象()执行类的 __call__ 方法
"""

# 创建元类，
class SingletonType(type):
	_instance_lock = threading.Lock()

	def __call__(cls, *args, **kwargs): # 这里的cls指的是Foo类
		if not hasattr(cls, "_instance"):
			with SingletonType._instance_lock:
				if not hasattr(cls, "_instance"):
					cls._instance = super().__call__(*args, **kwargs)
		return cls._instance

# Foo类使用SingletonType元类进行创建
class Foo(metaclass = SingletonType):
	def __init__(self, name):
		self.name = name


obj1 = Singleton()
obj2 = Singleton()
print(obj1)
print(obj2)

def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
	# 创建线程（target为需要线程去执行的方法名）
    t = threading.Thread(target=task, args=[i, ])
    # 启动线程
    t.start()

obj1 = Foo('name')
obj2 = Foo('na')
print(obj1.name,obj2.name)