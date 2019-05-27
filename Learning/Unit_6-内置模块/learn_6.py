import collections
import random
#================================================================
# 42. 用functools.wraps定义函数修饰器
#----------------------------------------------------------------
# 打印某个函数在受到调用时所接收的参数及该函数的返回值
#----------------------------------------------------------------
# from functools import wraps

# def trace(func):
# 	@wraps(func)
# 	def wrapepr(*args, **kwargs):
# 		result = func(*args, **kwargs)
# 		print('%s(%r,%r) -> %r' % (func.__name__, args, kwargs, result))
# 		return result
# 	return wrapepr

# @trace # 等效于 fibonacci = trace(fibonacci)
# def fibonacci(n):
# 	"""Test the help func"""
# 	if n in (0,1):
# 		return n
# 	return (fibonacci(n-2) + fibonacci(n-1))

# fibonacci(5)

# print(help(fibonacci))
#----------------------------------------------------------------


#================================================================
# 43. 考虑以contextlib和with语句来改写可复用的try/finally代码
#----------------------------------------------------------------
# import logging
# from contextlib import *

# def my_function():
# 	logging.debug('Some debug data')
# 	logging.error('Error log here')
# 	logging.debug('More dabug data')

# my_function()

# @contextmanager # 修饰器 可以在with中实现 try finally
# def debug_logging(level):
# 	logger = logging.getLogger()
# 	old_level = logger.getEffectiveLevel()
# 	logger.setLevel(level)
# 	try:
# 		yield
# 	finally:
# 		logger.setLevel(old_level)

# with debug_logging(logging.DEBUG):
# 	print("Before")
# 	my_function()
# print('After')
# my_function()
#----------------------------------------------------------------


#================================================================
# 44. 用copyreg实现可靠的pickle操作
#----------------------------------------------------------------
# 彼此不信任的人或程序之间，如果要进行通信，就应该使用JSON这样的格式
#----------------------------------------------------------------
class GameState(object):
	def __init__(self):
		self.level = 0
		self.lives = 4

#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 45. 应该用datetime模块来处理本地时间，而不是用time模块
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 46. 使用内置算法与数据结构
#----------------------------------------------------------------
# # 1. 双向队列 deque 从该队列的头部或尾部插入或移除一个元素 O(1)

# fifo = collections.deque()
# for i in range(5):
# 	fifo.append(2*i)
# x = fifo.popleft()
# y = fifo.popleft()
# print('x=',x,'y=',y,'fifo=',fifo)

# # 2. 有序字典 OrderedDict
# a = {}
# a['bar'] = 2
# a['foo'] = 1

# while True:
# 	z = 200
# 	b = {}
# 	for i in range(z):
# 		b[i] = i
# 	b['foo'] = 1
# 	b['bar'] = 2
# 	for i in range(z):
# 		del b[i]
# 	if str(b) != str(a):
# 		break

# print(a)
# print(b)
# print(a==b)

# a = collections.OrderedDict()
# a['foo'] = 1
# a['bar'] = 2
# b = collections.OrderedDict()
# b['foo'] = 'red'
# b['bar'] = 'blue'

# for value1, value2 in zip(a.values(), b.values()):
# 	print(value1, value2)

# # 3. 带有默认值的字典 defaultdict
# stats = {'my_counter':1,'2':2}
# key = 'my_counter'
# if key not in stats:
# 	stats[key] = 0
# stats[key] += 1
# print(stats)

# stats = collections.defaultdict(int)
# stats[key] += 1
# print(stats)

# # 4. 堆队列（优先级队列）heapq 
# from heapq import *

# a = []
# heappush(a, 5)
# heappush(a, 3)
# heappush(a, 7)
# heappush(a, 4)
# # 元素会按照优先级从高到低顺序从堆中弹出（数值较小的元素，优先级较高）
# print(a[0])
# print(a)
# a.sort()
# print('After:',a)
# print(heappop(a),heappop(a),heappop(a),heappop(a))
# print(a)

# # 5. 二分查找
# from bisect import *

# x = list(range(10**7))
# i = x.index(9991234)
# # i = bisect_left(x, 9991234)
# print(i)

#----------------------------------------------------------------


#================================================================
# 47. 在重视精度的场合，应该使用decimal
#----------------------------------------------------------------
# from decimal import *

# rate = 1.45
# seconds = 3*60+42
# cost = rate * seconds / 60
# print(cost)

# print(round(cost,2))

# rate = Decimal('1.45')
# seconds = Decimal('222')
# cost = rate * seconds / Decimal('60')
# print(cost)

# rounded = cost.quantize(Decimal('0.01'), ROUND_UP)
# print(rounded)
#----------------------------------------------------------------

