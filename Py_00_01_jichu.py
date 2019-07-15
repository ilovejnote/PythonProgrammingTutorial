# -*- coding: utf-8 -*-
# print absolute value of an integer

a = 100
if a >= 0:
	print(a)
else:
	print(-a)

# print string of \n...
# If there is '' in '' use \ to turn
print('I\'m "OK" !')
print('I\'m \"OK\" !')
# If there is enter in use \n to turn
print('I\'m Learning\nPython.')
print('\\\n\\')
print('\\\t\\')
# use r' or r'' or r''' to undo the \ turn action
print(r'\\\t\\')
# If there have lots of enter line then use ''' to use no \n
print('''line1
line2
line3''')

# Add homework at end

# -*- coding:utf-8 -*-
print(r'''hello,\n
world''')

# excercise  or  practice  The Bool value
print(True)
print(False)
print(3 > 2)
print(3 > 5)
# practice  Or  excercise The Bool math "and or not"
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)

print(True or True)
print(True or False)
print(False or False)
print(5 > 3 or 1 > 3)

print(not True)
print(not False)
print(not 1 > 2)
# practice or excercise The Bool math in if
age = 37
if age >= 18:
    print('adult')
else:
    print("teenager")

# practice or excercise the "None" So None != 0 So None is None
# Now no example for "None"

#Practice or excercise variable (variable's name use English Character Number and _ to work together)
a = 1
t_007 = "T007"
Answer = True
print(a, t_007, Answer)
print(a,t_007,Answer)
# In print if there is a , then print a " " out.
b = (a, t_007, Answer)
print(b)
c = [a, t_007, Answer]
print(c)
# The Python Programming language is dynamic language So the variable can change to integer then character
a = 123 # a is integer
print(a)
a = "ABC" # a change to strings
print(a)

# excercise or practice the "=" It is diffrent from the math's "="
a = "ABC"
b = a
a = 'XYZ'
print(b)
# So in math then to print out XYZ, But in python's "=",it is print out ABC

# practice or excercise the constant,for example PI(so the constant is usually use capital letters) while It names constant But if you go to change it .Then it changes. you must remember that.
PI = 3.14159265359
print(PI)
PI = 3.142
print(PI)

# practice or excercise the division in python.
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)


