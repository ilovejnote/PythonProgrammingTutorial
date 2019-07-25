# -*- coding: utf-8 -*-
# example in lesson fact(n)
def fact(n):
    if n == 1:
        return 1
    return n*fact(n - 1)

fact(5)
fact(100)
# But if fact(1000) will run out a wrong:   RecursionError: maximum recursion depth exceeded in comparison.
# Add homework after class.
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)
        
    