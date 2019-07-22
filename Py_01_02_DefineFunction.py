# -*- coding: utf-8 -*-
# If you want to define a function for yourself. To use def and the function's name and () and : Then use return to take back the value of function.
# for example in tutorial.
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
print(my_abs(-99))

# attention that inside the functions, when run to the syntax return then function runs over. take back the value by return.
# If you save the function of my_abs() by a file named abstest.py . Then you can start the python in the content of this file.and use
# "from abstest import my_abs" attention that "abstest" not "abstest.py"


# If you want to define a function But to do nothing. then use syntax "pass". for example.
def nop():
    pass
# infact "pass" is a function of take a set. when you want to add some code after . But now add pass the code can run now.
# for example pass can use in other syntax . As If syntax.
if age >= 18:
    pass
# if there is no pass Then the code will run wrong out.

# THE CHECK OF THE ARGUMENT.
# When invoking functions. If the argument's number is not correct .the interpreter of python will check it out and report a TypeError.
# for example
# >>> my_abs(1, 2)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: my_abs() takes 1 positional argument but 2 were given
# But if the type of the argument not correct. The interpreter of python can not check it out.
# for example:
# >>> my_abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in my_abs
# TypeError: unorderable types: str() >= int()
# >>> abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: bad operand type for abs(): 'str'
# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# When you add argument check then the Wrong type of argument can report out.
# for example:
# >>> my_abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in my_abs
# TypeError: bad operand type

# Can the functions take back more than one values ? The answer is CAN.
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)
# >>> x, y = move(100, 100, 60, math.pi / 6)
# >>> print(x, y)
# 151.96152422706632 70.0
# 但其实这只是一种假象，Python函数返回的仍然是单一值：
# >>> r = move(100, 100, 60, math.pi / 6)
# >>> print(r)
# (151.96152422706632, 70.0)
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回#多值其实就是返回一个tuple，但写起来更方便。
