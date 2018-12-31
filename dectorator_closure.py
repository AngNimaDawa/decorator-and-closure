
#it helps to define function in function
#it helps pass in function
#it helps return function in function


# def hello():
# 	"""
# 	This is the enclosing function
# 	"""
# 	message = 'hello python'
# 	def greet():
# 		print('greet: ',message)
# 	greet()
# hello()

#closure with return
#function return function

# def hello():
# 	"""
# 	this is the enclosing function
# 	"""
# 	message = 'hello python'
# 	def greet():
# 		print('greet: ',message)
# 	return greet
# gr = hello() #valid for callable object onlyi.e.hello should return callable function
# gr()

# greet1 = hello #here hello is assigned to greet1 here calling greet1 hence calling greet1 calls hello and return greet.
# say_hello =greet1()
# say_hello()

#function take function as argument
# def hello(func):
# 	print('im hello function')#
# 	if callable(func):
# 		func()# actualy greet is calling
# def greet():
# 	print('im greet function')
# hello(greet)#as we always pass argument in function which is object and here we can pass function which shows function is an obj which is called 1st class obj.


#decorator 
#it helps to function without deleting the obj

# def greet():
# 	return 'nima sherpa'
# print(greet())

# def decorator(func):
# 	def wrapper():
# 		r = func()
# 		return '<h1>' + r + '</h1>'
# 	return wrapper
# def greet():
# 	return 'nima sherpa'
# greet()

# dgreet = decorator(greet)
# print(dgreet())


# def tag_h1(func):
# 	def wrapper():
# 		r = func()
# 		return '<h1>' + r + '</h1>'
# 	return wrapper
# def greet():
# 	return 'nima sherpa'
# greet()

# dgreet = tag_h1(greet)
# print(dgreet())


#def h1(func):
# 	def wrapper():
# 		return '<h1>' + func()+'</h1>'
# 	return wrapper
# @h1 #it show the same result of h1(greet) and it is new update version
# def greet():
# 	return 'nima sherpa'

# #greet = h1(greet) #it is a old version of decorator
# print(greet())

def h1(func):
	def wrapper(*args, **kwargs):
		return'<h1> {} </h1>'.format(func(*args,**kwargs))
	return wrapper
@h1

def greeting(name):
	return 'hello {} goodmorning!.format(name)'
print(greeting('nima'))
