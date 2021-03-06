#================================================================
# 49. 为每个函数、类和模块编写文档字符串 
#----------------------------------------------------------------
def palindrome(word):
	"""
	如果传入的word为回文 返回True
	例如 eye True
		 white False 
	"""
	return word == word[::-1]

print(palindrome('eye'))
print(palindrome('wewe'))
print(repr(palindrome.__doc__))
#----------------------------------------------------------------


#================================================================
# 51. 为自编的模块定义根异常，以便将调用者与API相隔离
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 52. 用合适的方式打破循环依赖关系
#----------------------------------------------------------------
# 1. 调整引入顺序
# 2. 先引用、再配置、最后运行
# 3. 动态引入（尽量不用 循环import会有奇怪的错误）
#----------------------------------------------------------------


#================================================================
# 53. 用虚拟环境隔离项目， 并重建其依赖关系
#----------------------------------------------------------------
# pyvenv 虚拟环境
# 在阿里云上购买的Django的镜像中使用的 
#----------------------------------------------------------------


