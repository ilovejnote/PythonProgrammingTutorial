# -*- coding: utf-8 -*-
# invoking function or call function in python.
# Let's take a built-in function for example. to invoking a function we need to know the function's name and argument.


# >>> help(abs)
# Help on built-in function abs in module builtins:
# 
# abs(x, /)
#     Return the absolute value of the argument.
#
# >>> 


# From the help() we know that the abs() just have one argument. If you use two of this .then python will run wrong out.


# >>> abs(1, 2)
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     abs(1, 2)
# TypeError: abs() takes exactly one argument (2 given)
# >>> 


# Then the Number of argument is right ,But If the type of argument is not right .like down


# >>> abs('a')
# Traceback (most recent call last):
#   File "<pyshell#4>", line 1, in <module>
#     abs('a')
# TypeError: bad operand type for abs(): 'str'
# >>> 


# function of max() can receive mount of arguments and take back the biggest one .
print(max(1, 2, 3))
print(max(1, 1.5, 3, -5))
# function of change the type of data.
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
# the name of function is really the quote of the function's oop point to . So you just can put a function's name to a variable.
a = abs # variable a point to the function of abs
print(a(-1))

# Add homework at endswith

n1 = 255
n2 = 1000
print(hex(n1),hex(n2))
# know soem usually number 
n3 = 1024
n5 = 4096
n6 = 65535
print(hex(n1), hex(n3), hex(n5), hex(n6))
