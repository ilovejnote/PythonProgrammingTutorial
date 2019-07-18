# -*- coding: utf-8 -*-
# python inside the support of dict(dictionary), In other language they called it map. use (key-value) to store. quickly for look up.
# for example first to use list, then we need two lists
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
name = input('Please enter the name for lookup:')
for i in range(3):
    if names[i] == name:
        index = i
if name in names:
    print('Your name is %s, And your scor is %s' % (name, scores[index]))
else:
    print('Your enter name is not found, Please check out and try again.')
    
# second method
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
name = input('Please enter the name for lookup:')
index = False
for i in range(3):
    if names[i] == name:
        index = i
        print('Your name is %s, And your scor is %s' % (name, scores[index]))
if index == False:
    print('Your enter name is not found, Please check out and try again.')

# -*- coding: utf-8 -*-
# To use dict (dictionary) you should use {} and : to setup it .
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print(d['Michael'])
# When you want to put a value in the dict you have two ways .first use init ditc. Second use set value to put in .
d['Adam'] = 67
print(d)
print(d['Adam'])
# Because one key must have one value. the if you time after time to put difference value in a key . then the last value worked.
d['Jack'] = 90
print("d['jack'] is :", d['Jack'])
d['Jack'] = 88
print("d['jack'] is :", d['Jack'])
# If the key is not exist, then the python will run wrong out. two ways to save it .one : use in .two :use get()
print('Thomas' in d)
d.get('Thomas', -1) # If there no argument after , then get()will take back Like None value . If you want take a point value then add it afer ,.
# If you want to delete a key , use pop(key) method.
d.pop('Bob')
print(d)
# attention there in no order in the dict. and the key in dict can not changed. list can not use to key.
# As set is like dict. But set can not store value. it always save a key at all.
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
# Talk about again can not changed oop.
# first this is can changed.
a = ['c', 'b', 'a']
print(a)
print(a.sort())#!!!print a None
c = a.sort()
print(c)
# second this is can not changed.
a = 'abc'
print(a)
print(a.replace('a', 'A'))
b = a.replace('a', 'A')
print(b)
print(a)



