# -*- coding: utf-8 -*-
# The Arguments of the Functions. There are five method of python's arguments. 
# There are required argument, default argument, changed argument, key-words argument.
# 位置参数 for example funcion for calculate x * x
def power(x):
	return x * x
# To power(x) the argument x is a position argument. When we invoking the power(x) 
# then we must give one and just one argument x.
s = power(5)
print(s)
s1 = power(15)
print(s1)
# Now let's try to setup function to calculate x **n ,call it power(x, n)
def power(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

s2 = power(5, 2)
print(s2)
s3 = power(5, 3)
print(s3)

# There the power(x, n) the two of the argument is the position argument. 
# When invoking the function we must give in order the two argument.
# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
s5 = power(5)
print(s5)
s6 = power(5, 2)
print(s6)
# When setup the default argument attentiion two points.
# first : the required position argument must set at front. 
# second: the default arguments if have more than one .Then put the change most at front and go on. and the lest changed argument set the default.
# So what the advantage for set the default argument? The answer is less the hard of invoking the functions.
# for example:
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
enroll('Sarah', 'F')
# add more example:
def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city = 'Tianjin')
# Something should to be attention. first define a function . take in a list , then add an "END" and bring back.
def add_end(L = []):
    L.append('END')
    return L
add_end([1, 2, 3])
add_end(['x', 'y', 'z'])
add_end()
add_end()
# When you use the default argument, Then the python likes remember the last value. It add "END" time and time.
# explanation the reason.the default argument L's value was calculate out beyond the invoking. So when you invoking the function
# The default argument L's value is changed.
# So attention that @@@ the default argument's value must point to no change oop. @@@
# And we can change the code to OK.
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
add_end()
add_end()
# avoid adding wrong code , you should always use the no change values in default argument.


# Learning variable parameter.
# As it says ,the arguments numbers can be 0, 1, 2,...
# for example: in math we have a ** 2 + b ** 2 + c **2 ...
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# But for invoking we need to install a list or tuple:
calc([1, 2, 3])
calc((1, 3, 5, 7))
# Then use the variable parameter we can short code like this:
calc(1, 2, 3)
calc(1, 3, 5, 7)
# Down to type the code.(variable parameter)
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# compare to the old function .The variable parameter only need add a *.then in the function it take a tuple.
# after add a * .Then you can bring in any numbers of time.
calc(1, 2)
calc()
# But if there alreay have a list or tuple. Then how to invoking a variable parameter?
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
# For short of code you can type like down:
calc(*nums)
# For this type of code is very useful And also very usually.


# Key-world argument, In variable parameter you can take 0 or any numbers of argument. But Key-worlds let you take in 0 or any
# include name of argument. these key-words argument in functions inside setup a dict.
# for example:
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# Then when you invoking the functions you can just take the required argument.
person('Michael', 30)
# And you can take in any time of you wants argument.
person('Bob', 35, city = 'Beijing')
person('jite', 37, city = 'Qinhuangdao', programming = 'Python')
# What is the key-words doing in python: That we say the function can take two arguments. But if user want to bring more information
# We also can receive by key-words argument.
# Like up -> variable parameter this key-words argument can first setup a dict then turn the dict to key-words and bring it in.
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city = extra['city'], job = extra['job'])
# We can short code like down:
person('Jack', 24, **extra)
# The **extra to take the extra dict all the values by key-words argument and take it one by one . 
# And the kw get a copyer of extra. the change to the kw can not go on to the extra dict that out of the function.
# 
# 
# name key-words argument : for key-words argument invoker can take in whatever parameter they like .
# But in the end what parameter being take in . We need to check it in the function from kw.
# for example: person()
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
# But like up , invoker also can take any of parameters.
person('Jack', 24, city = 'Beijing', addr = 'Chaoyang', zipcode = 123456)
# Then if you want to ask the invoker to use the named argument.
# for example, only take 'city' and 'job' as key-words argument.
def person(name, age, *, city, job):
    print(name, age, city, job)
# Difference from the key-words argument the named key-words argument use the * as a separator
person('Jack', 24, city = 'Beijing', job = 'Engineer')
# So the named key-words argument must take in the parameter's name. or the python interpreter will bring wrong out.
#for example:
#person('Jack', 24, 'Beijing', 'Engineer')
#>>> person('Jack', 24, 'Beijing', 'Engineer')
#Traceback (most recent call last):
#  File "<pyshell#48>", line 1, in <module>
#    person('Jack', 24, 'Beijing', 'Engineer')
#TypeError: person() takes 2 positional arguments but 4 were given
# The named key-words argument also can have default parameter values . And this is for easy.
def person(name, age, *, city ='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job = 'Engineer')
# The other type: If there is a variable parameter then you can not put the separator *.
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

    
# The complex of arguments.
# there are the five type of python's arguments. then you can use them at the same time . But please in order 
# the order is 1) the required argument 2) the default argument 3)variable argument 4)named key-words argument 5) key-words argument.
# for example:
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
f1(1, 2, 3)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
f2(1, 2, d = 99, ext = None)
# Amazing that for tuple or dict you also can bring up functions.
args = (1, 2, 3, 4)
kw = {'d':99, 'x':'#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d':88, 'x':'#'}
f2(*args, **kw)

# add homework after lesson.
def product(*y):
    if y == None:
        return TypeError
    sum = 1
    for n in y:
        sum = n * sum 
    return sum
# test
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败')
elif product(5, 6) != 30:
    print('测试失败')
elif product(5, 6, 7) != 210:
    print('测试失败')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败')
else:
    try:
        product()
        print('测试失败')
    except TypeError:
        print('测试成功')




