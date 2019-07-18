# -*- coding: utf-8 -*-
# practice or exercise String and Encoding. Like ASCII, UTF-8, GB2312, Unicode...

print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
x = b'ABC'
print(x)
x1 = 'ABC'.encode('ascii')
print(x1)
x2 = '中文'.encode('utf-8')
print(x2)
# Then need to decode to print out for men
print(x1.decode('ascii'))
print(x2.decode('utf-8'))
print(x1.decode('utf-8'))
# then the "print(x2.decode('ascii'))"" will run wrong to the reson that Chinese can't encode to ascii.
# practice or excercise some code the python decode can not work then you should use decode's errors='ignore'
x3 = b'\xe4\xb8\xad\xe6\x96\x87'
print(x3.decode('utf-8', errors='ignore'))
# then use worng encode number As you use the decode's errors='ignore' your code will run with wrong encode.
x4 = b'\xe4\xb8\xad\xe6\xff\x87'
print(x4.decode('utf-8', errors='ignore'))

# When you want to count the letters in the Strings. Then use the len() Down to practice or exercise.
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
# Make sure you to encode the letters using UTF-8 you need type down text like this as down text.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# the first line to tell Linux/OS X system , This is a Python exe application As if you using windows system will to be ignore.
# the second line to tell Python interpreter to read the souce code as UTF-8 encode.

# FORMAT the string in print . To use %. now to practice or exercise.
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michal', 1000000))
# %d, %f, %s, %x the four of charactor are the most using in the print()
# As you use integer and float you also can add integer '0' or control the float's numbers.
print('%5d-%05d' % (3, 1))
print('%.2f' % 3.1415926)
# If you are not sure to use integer or string Then you can use the String (%s) It always to be using.
print('Age: %s. Gender: %s' % (25, True))
# Then if there need a '%' to stand as a normal charactor. you need to use %% to print it out .
print('growth rate: %d %%' % 7)
# there is another method to format string in the print . To using format()
print('Hello,{0}, 成绩提升了{1:.1f}%' .format('小明', 17.125))

# add homework at the endswith
s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
print('小明的成绩从去年的72分提升到了今年的85分，小明成绩提升的百分点是%.2f%%.' % r)




