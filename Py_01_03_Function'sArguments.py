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
