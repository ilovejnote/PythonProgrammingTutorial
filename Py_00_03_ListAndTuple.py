# -*- coding: utf-8 -*-
# init a list variable and print it out
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# use len() can counts the number of the list .
print(len(classmates))
# How to index the number of the list
i = 0
while i<= (len(classmates ) - 1):
    print(classmates[i])
    i = i + 1
#another method of index list
print(classmates[0], classmates[1], classmates[2])
print(classmates[-1], classmates[-2], classmates[-3])
# List insert append pop change methods
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
# use pop() to delete the last member
classmates.pop()
print(classmates)
# use pop(i) to delete the i member
print(classmates[1])
classmates.pop(1)
print(classmates)
# to change member's value use index and =
classmates[1] = 'Sarah'
print(classmates)
# In the list , these members can be diffrents , they can be integer float string or list and bool
L = ['Apple', 123, True, 456.789, ['a', 1, False], 'Linux']
print(L)
# And the list is one member , you can use the len() to count it out.
print(len(L))

# Next we go and see tuple
# tuple is very like list ,But tuple once built up it can not change. tuple do not have the method of 
# insert() append() pop() and use index = to change.
Classmates = ('Apple', 'Orange', 'Pear', 'banana', 'watermelon')
print(Classmates)
# attension to the tuple's trap that you can not to use t = (1) to set up a one member tupel.
# to set up a one member tupel to use t = (1,) to done. So the first t is integer. the second t as tuple.
t = (1)
print(t)
t1 = (1,)
print(t1)
# As you want to set up a None tuple you can use the t = ()
t = ()
print(t)
# In the end we see a tuple that look like it can change .But in fact it not change. Down at 
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
# explaination : change in fact occur in the list. the tuple is not change. Also you can say that
# The tuple not change is that the points of tuple is not change.

# Add homework of the lesson at the end
L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
# print Apple:
print(L[0][0])
# print Python:
print(L[1][1])
# print Lisa:
print(L[2][2])



