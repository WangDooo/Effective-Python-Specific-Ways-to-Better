import datetime
import time

#================================================================
# 15. 了解如何在闭包里使用外围作用域中的变量
#----------------------------------------------------------------
# numbers = [8,3,1,2,5,4,7,6]
# group = {2,3,7,5} # 这个要优先排列的

# def sort_priority(values, group):
# 	def helper(x):
# 		if x in group:
# 			return (0,x)
# 		return(1,x)
# 	values.sort(key=helper)
# 	# 在调用列表的sort方法时，把辅助函数传给key参数，这个辅助函数的返回值，将会用来确定列表中各元素的顺序
# sort_priority(numbers,group)
# print(numbers)

# # 获取闭包中的数据
# # （1）失败的，作用域bug，局部变量, None
# def sort_priority2(values, group):
# 	found = False
# 	def helper(x):
# 		if x in group:
# 			found = True
# 			return (0,x)
# 		return(1,x)
# 	values.sort(key=helper)
# 	return found
# found = sort_priority2(numbers,group)
# print(numbers,'Found:',found)

# # （2）使用nonlocal  与global语句互为补充，除了比较简单的函数，尽量不要用nonlocal
# def sort_priority3(values, group):
# 	found = False
# 	def helper(x):
# 		nonlocal found
# 		if x in group:
# 			found = True
# 			return (0,x)
# 		return(1,x)
# 	values.sort(key=helper)
# 	return found
# found = sort_priority3(numbers,group)
# print(numbers,'Found:',found)

# # （3）封装成辅助类 与nonlocal效果一样
# class Sorter(object):
# 	def __init__(self,group):
# 		self.group = group
# 		self.found = False
# 	def __call__(self,x):
# 		if x in self.group:
# 			self.found = True
# 			return (0,x)
# 		return (1,x)

# sorter = Sorter(group)
# numbers.sort(key=sorter)
# print(numbers,'Found:',sorter.found)

# # （4）利用作用域
# def sort_priority4(values, group):
# 	found = [False]
# 	def helper(x):
# 		nonlocal found
# 		if x in group:
# 			found[0] = True
# 			return (0,x)
# 		return(1,x)

# 	values.sort(key=helper)
# 	return found[0]
# found = sort_priority3(numbers,group)
# print(numbers,'Found:',found)
#----------------------------------------------------------------


#================================================================
# 16. 考虑用生成器来改写直接返回列表的函数
#-----------------------------------------------------
# address = "Four score and seven years ago"
# def index_words_iter(text):
# 	if text:
# 		yield 0
# 	for index, letter in enumerate(text):
# 		if letter == ' ':
# 			yield index + 1
# result = list(index_words_iter(address))
# print(result)
#----------------------------------------------------------------


#================================================================
# 17. 在参数上面迭代时，要多加小心
# 迭代器只能产生一轮结果
# 新编一种实现迭代器协议的容器类
#----------------------------------------------------------------
# def normalize(numbers):
# 	total = sum(numbers)
# 	result = []
# 	for values in numbers:
# 		percent = 100 * values / total
# 		result.append(percent)
# 	return result

# def read_visits(data_path):
# 	with open(data_path) as f:
# 		for line in f:
# 			yield int(line)
# path = '../tmp/my_numbers.txt'
# # it = read_visits(path)
# # print(list(it))
# # print(list(it))

# class ReadVisits(object):
# 	def  __init__(self, data_path):
# 		self.data_path = data_path

# 	def __iter__(self):
# 		with open(self.data_path) as f:
# 			for line in f:
# 				yield int(line)

# path = '../tmp/my_numbers.txt'
# visits = ReadVisits(path)
# percentages = normalize(visits)
# print(percentages)
#---------------------------------------------------------------


#================================================================
# 18. 用数量可变的位置参数减少视觉杂讯 *args
#----------------------------------------------------------------
# def log(message, *values):
# 	if not values:
# 		print(message)
# 	else:
# 		values_str = ', '.join(str(x) for x in values)
# 		print(message, values_str)

# log('My ID:', 23,45,89)
# log('No ID')

# test = [12,89,45,78]
# log('Test:', *test) # 加星就是把列表里的元素视为位置参数
#----------------------------------------------------------------


#================================================================
# 19. 用关键字参数来表达可选的行为 阐明每个参数的用途
#----------------------------------------------------------------
# def remainder(number, divisor):
# 	return number % divisor

# print(remainder(10,3))
# print(remainder(10, divisor=3))
# print(remainder(divisor=3, number=10))
# print(remainder(number=10, divisor=3))
#----------------------------------------------------------------


#================================================================
# 20. 用None和文档字符串来描述具有动态默认值的参数
# 参数的默认值， 只会在程序加载模块并读到本函数的定义时评估一次
#----------------------------------------------------------------
# def log(message, when=None):
# 	when = datetime.datetime.now()
# 	print(when, message)

# log('Hi There')
# time.sleep(1)
# log('Hi that')
#----------------------------------------------------------------


#================================================================
# 21. 用只能以关键字形式指定的参数来确保代码清晰
#----------------------------------------------------------------
def safe_divison(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
	try:
		return number / divisor
	except OverflowError:
		if ignore_overflow:
			return 0
		else:
			raise
	except ZeroDivisionError:
		if ignore_zero_division:
			return float('inf')
		else:
			raise

result = safe_divison(1.0, 10**500, ignore_overflow=True)
result = safe_divison(1.0, 0, ignore_zero_division=True)
print(result)
#----------------------------------------------------------------


