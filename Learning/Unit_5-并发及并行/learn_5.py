from time import time
from threading import Thread
from threading import Lock 

#================================================================
# 36. 用subprocess模块来管理子进程
#----------------------------------------------------------------
# import subprocess
# from time import time

# proc = subprocess.Popen(['echo', 'Hello world'], stdout=subprocess.PIPE)
# out, err = proc.communicate()
# print(out.decode('utf-8'))

# def run_sleep(period):
# 	proc = subprocess.Popen(['sleep', str(period)])
# 	return proc

# start = time()
# procs = []
# for _ in range(10):
# 	proc = run_sleep(0.1)
# 	procs.append(proc)

# for proc in procs:
# 	proc.communicate(timeout=0.5)
# end = time()
# print("Finished in %.3f s" % (end-start)) 
#----------------------------------------------------------------


#================================================================
# 37. 可以用线程来执行阻塞式I/O，但不要用它做平行计算
#----------------------------------------------------------------

# def factorize(number):
# 	for i in range(1, number+1):
# 		if number % i == 0:
# 			yield i

# numbers = [2131332, 1324132, 1898989, 1078932]
# start = time()
# for number in numbers:
# 	list(factorize(number))
# end = time()
# print('Took %.3f s' % (end-start))



# class FactorizeThread(Thread):
# 	def __init__(self, number):
# 		super().__init__()
# 		self.number = number

# 	def run(self):
# 		self.factors = list(factorize(self.number))

# start2 = time()
# threads = []
# for number in numbers:
# 	thread = FactorizeThread(number)	
# 	thread.start()
# 	threads.append(thread)

# for thread in threads:
# 	thread.join()

# end2 = time()
# print('Took %.3f s' % (end2-start2))

# import select
# from threading import Thread

# select.select
# def slow_systemcall():
# 	select.select([],[],[],0.1)

# start = time()
# for _ in range(5):
# 	slow_systemcall()
# end = time()
# print('Took %.3f s' % (end-start))

# start = time()
# threads = []
# for _ in range(5):
# 	thread = Thread(target=slow_systemcall)
# 	thread.start()
# 	threads.append(thread)

# for thread in threads:
# 	thread.join()
# end = time()
# print('Took %.3f' % (end-start))
#----------------------------------------------------------------


#================================================================
# 38. 在线程中使用Lock来防止数据竞争
#----------------------------------------------------------------
# class Counter(object):
# 	def __init__(self):
# 		self.count = 0

# 	def increment(self, offset):
# 		self.count += offset

# def worker(sensor_index, how_many, counter):
# 	for _ in range(how_many):
# 		# Read from the sensor
# 		counter.increment(1)

# def run_threads(func, how_many, counter):
# 	threads = []
# 	for i in range(5):
# 		args = (i, how_many, counter)
# 		thread = Thread(target=func, args=args)
# 		threads.append(thread)
# 		thread.start()
# 	for thread in threads:
# 		thread.join()

# class LockingCounter(object):
# 	def __init__(self):
# 		self.lock = Lock() # 互斥锁
# 		self.count = 0

# 	def increment(self, offset):
# 		with self.lock:
# 			self.count += offset

# how_many = 10**5
# counter = LockingCounter()
# run_threads(worker, how_many, counter)
# print('Counter should be %d, found %d' % (5*how_many, counter.count))
#----------------------------------------------------------------


#================================================================
# 39. 用Queue来协调各线程之间的工作
#----------------------------------------------------------------
# 采用函数管线 pipeline 协调同时执行的许多事物
# 任务传递方式 生产-消费队列 producer-consumer queue

import collections

class MyQueue(object):
	def __init__(self):
		self.items = collections.deque()
		self.lock = Lock()

	def put(self, item):
		with self.lock:
			self.items.append(item)

	def get(self):
		with self.lock:
			return self.items.popleft()

class Worker(Thread):
	def __init__(self, func, in_queue, out_queue):
		super().__init__()
		self.func = func
		self.in_queue = in_queue
		self.out_queue = out_queue
		self.polled_count = 0
		self.work_done = 0
	def run(self):
		while True:
			self.polled_count += 1
			try:
				item = self.in_queue.get()
			except IndexError:
				sleep(0.01) # No work to do
			else:
				result = self.func(item)
				self.out_queue.put(result)
				self.work_done += 1

myqueue = MyQueue()
#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------