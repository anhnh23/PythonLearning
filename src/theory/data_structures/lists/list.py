'''
Created on Dec 7, 2016

@author: ToOro
'''
from _ast import arguments
"""note: insert, remove and sort that only modify list have no return
value printed. They return None. This is design principle for all mutable data
structures in Python.
"""
a = [63, 22, 74.3] # this is structure of list with []

# List as a stack: Last-in, first-out
a.append(23) #last-in
a.pop() #first-out 23 will be remove

# List as a queues: First-in, first out
from collections import deque
queue = deque(a) # deque is built for fast appending and popping
queue.append(100)
queue.popleft() # remember popleft for first-out, if we use pop() it becomes last-out
print (queue)

# 3 Useful tools: filter(), map(), and reduces()
"""
filter(function, sequence): return a sequence consisting of those items from the sequence for which
    function(item) is true. If it sequence is a str, unicode or tuple, the result 
    will be of the same type; otherwise, it is always a list.
"""
def f(x): return x % 3 == 0 or x % 5 == 0
filter(f, range(2, 20)) # Result: [3, 5, 6, 9, 10, 12, 15, 18]
"""
map(function, sequence) return a list of return values
"""
def cube(x): return x*x*x
print (map(cube, range(1, 5))) # Result: [1, 8, 27, 64]

seq = range(5)
def add(x, y): return x+y
print (map(add, seq, seq)) # loop 2 sequences at the same time and do add, Resutl: 0, 2, 4, 6, 8

