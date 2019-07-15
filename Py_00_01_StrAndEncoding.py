# -*- coding: utf-8 -*-
# practice or excercise String and Encoding. Like ASCII, UTF-8, GB2312, Unicode...

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
