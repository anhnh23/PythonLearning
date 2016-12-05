'''This shows basic things during program with python
'''

""" ---------- Keywords and meaning
raise - to raise an exception
with - to alternative to the try/finally
def - declare a function
yeild - generator
"""

"""---------- Keywords and noting
else - also be used to do the false of 'while' and 'for' loop
pass - Python COMPOUNT STATEMENT (but not for def or class) cannot be empty (pass is used)
"""

""" ---------- Notes:
+ Flat is better than Nested
    - Using continue keyword is better than using nested loop.
+ Empty def or class statements: use a docstring, not pass
+ Functions:
    - They are objects (values)
    - They can also be keys into a dictionary
"""

"""----------Unorganized
"""
#Lambda Example
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
high = 7
filter(lambda x, l=low, h=high: h>x>l, a_list)

#Lambda with local def
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
hight = 7
def within_bounds(value, l=low, h=hight):
    return h>value>l
filter(within_bounds, a_list)

"""Generator function
Syntax:
1. for avariable in somegenerator(arguments):
2. resulting_list = list(G(arguments)) <-- bounded generator

NOTES:
+ Generator is more flexible than functions
"""
#Example
def updown(N):
    for x in range(1, N):
        yield x
    for x in range(N, 0, -1):
        yield x
for i in updown(3): print(i) #prints: 1 2 3 2 1

#Generator works like build-in range, but return an iterator
step = 2
def frange(start, stop, stride=1.0):
    while start < stop:
        yield start
        start += step
        
#Recursion
def rec(t):
    yield t[0]
    for i in (1,2):
        if t[i] is not None: yield from rec(t[i])
        

#Stack
def norec(t):
    stack = [t]
    while stack:
        t = stack.pop()
        yield t[0]
        for i in (2,1):
            if t[i] is not None: stack.append(t[i])