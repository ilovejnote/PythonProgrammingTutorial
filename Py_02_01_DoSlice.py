# -*- coding: utf-8 -*-
# for example in class (can use in list tuple str)
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack' ]
# To print The first three elements.
print([L[0], L[1], L[2]])
# This is a slow method. Becasue if you want take The first N (bigger number) elements, it is will be very impossible
# For this time you can use circulation to index The first N (bigger number) elements.
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# for in this case: python give a Slice method.
print(L[0:3])
# And also you can start index from The first or the second element.
print(L[1:3])
# Then If you start from the First element. You also can short the code like this.
print(L[:3])
# Also you can index it by count backwards. now that python give L[-1], So you can Slice the list in this way.
print(L[-2:])
# print out ['Bob', 'Jack']
print(L[-2:-1])
# print out ['Bob']
# Then test slice the list : for example
L = list(range(100))
print(L)
# Use slice take out one passage out:
print(L[:10])
print(L[-10:])
# print out 10-20
print(L[10:21])
# print out the first ten elements, and take one every two.
print(L[:10:2])
# print out all of the elements, and take one every five.
print(L[::5])
# Also you can type nothing to copy a total list.
print(L[:])


# And tuple can be another type of list. Although tuple can not changed.
print((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)[:3])
# Then then str can also take it as a list. Every character can be a element.
print('ABCDEFG'[:3])
# It print out ABC

# Add homework after class.
def trim(s):
    if len(s) == 0:
        return ''
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-2])
    else:
        return s
# test
if trim('hello ') != 'hello':
    print('测试失败！')
elif trim(' hello') != 'hello':
    print('测试失败！')
elif trim(' hello ') != 'hello':
    print('测试失败！')
elif trim(' hello world ') != 'hello world':
    print('测试失败！')
elif trim('') != '':
    print('测试失败！')
elif trim('   ') != '':
    print('测试失败！')
else:
    print('测试成功！')
# up was wrong ,not control the [:-1], I write [:-2]. So the right code is down:
def trim(s):
    if len(s) == 0:
        return ''
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s
# test
if trim('hello ') != 'hello':
    print('测试失败！')
elif trim(' hello') != 'hello':
    print('测试失败！')
elif trim(' hello ') != 'hello':
    print('测试失败！')
elif trim(' hello world ') != 'hello world':
    print('测试失败！')
elif trim('') != '':
    print('测试失败！')
elif trim('   ') != '':
    print('测试失败！')
else:
    print('测试成功！')
