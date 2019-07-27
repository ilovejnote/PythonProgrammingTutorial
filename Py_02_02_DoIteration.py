# -*- coding: utf-8 -*-
# If given a list or tuple, we can use "for" to Iteration this type of data. we called this Iteration.
# In python we use "for ... in " to work out.
# for example like dict
d = {'a':1, 'b':2, 'c':3}
for key in d:
	print(key)
# This dict not orderable data, so The print out order can be diffrence from the dict.
# In the usually way the Iteration use the key  if use value "for value in d.values()" if at the sametime
# "for k, v in d.items()"
for ch in 'ABC':
	print(ch)

# The method of judge if the data can be Iteration. use "collections" Module's Iterable type .
from collections import Iterable
Iabc = isinstance('abc', Iteable)
Idatas = isinstance([1, 2, 3], Iteable)
Id = isinstance(123, Iterable)
print(Iabc, Idatas, Id)


# How to index the list , python use "enumerate" to change a list to a Index elements. Then can do .
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

L1 = list(range(1,1000))
for i, value in enumerate(L1):
	print(i, value)
