# -*- coding: utf-8 -*-
# important function of computer is always 'circulation' in python there are for ... in ... and while 
# first python circulation is for ... in ... it can iteration every element from in...(list or tuple)
# for example calculate 1 + 2 + 3 you can manual write down the code like down
print(1 + 2 + 3)
# But if we need to calculate 1 + 2 + 3 +.....100 ,or 10000 we must use the circulation syntax.
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
# I say that to make out a big list we usualy use range() function.
print(list(range(5)))
# range(x) can make out from 0 to x -1 numbers. so the calculate 1 + 2 + 3 +.....100 , we can make like this
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# The second circulation is while . In while if the conditional is alright. then the cirulation is go on. 
# So you must add a variable to cut itself down. then can out of cirulation.
# for example
sum = 0
n = 100
while n > 0:
    sum = sum + n 
    n = n - 1
print(sum)
# change the code to calculate even number's sum.
sum = 0
n = 100
while n > 0:
    sum = sum + n 
    n = n - 2
print(sum)

# practice in the class 
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('Hello,', i)

# Add break or continue in the circulation syntax. then you can run out of the circulation by break. and out of circulation once by continue.
# for example break
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
# Then if you want to shut down the circulation in the middle. you can use the break syntax. and also should use if syntax
# first example break:
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
# second example continue:
# like this down : I write a bad circulation . It calls endless loop. it print out '1' then can not run out of the circulation.
#n = 1
#while n <= 100:
#    if n % 2 == 0:
#        continue
#    print(n)
#    n = n + 1
#print('END')
#---The right method is this:
n = 0
while n < 100:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('END')
# There is no homework at the end of the lesson.



