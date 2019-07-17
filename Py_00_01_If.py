# -*- coding: utf-8 -*-
# conditional judgment practice or exercise. if 
# The computer can do lots of work by auto , because that it can use conditional judgment in python call it if .
age = 20
if age >= 18:
    print('your age is ', age)
    print('adult')
# Then change the age to user input so the program can be little usefull.
age = input('Please enter you age:')
age = int(age)
if age >= 18:
    print('your age is ', age)
    print('adult')
else:
    print('your age is ', age)
    print('teenager')
# want to short the code, you can like this down
age = input('Please enter you age:')
age = int(age)
print('your age is ', age)
if age >= 18:
    print('adult')
else:
    print('teenager')
#So if you want to add more conditional Then you can use elif to add and add more elif if you want.
age = input('Please enter your age:')
age = int(age)
print('Your age is ', age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# You should attention that If ran from up to down. Because If run the first the value of bool is True and ignore others. So if you condition order not correct then some thing will be wrong. Like down 
age = 20
print('Your age is :', age)
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
# So if can short write like this :down
if True:
    print('True')
# Now tall about input, The input() take back string from user enter .So when you use the if and input at the same time you should use int().
s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# Add the homework at the end.
# -*- coding: utf-8 -*-
# calculate the BMI (weight division the square of height)
XMheight = 1.75
XMweight = 80.5
XMbmi = XMweight / (XMheight ** 2)
if XMbmi < 18.5:
    print('过轻')
elif XMbmi < 25:
    print('正常')
elif XMbmi < 28:
    print('过重')
elif XMbmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
# change the code use input()
height = input('Please enter your height in meter:')
weight = input('Please enter your weight in kilogram')
height = float(height)
weight = float(weight)
bmi = weight / (height ** 2)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

