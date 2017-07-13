'''
Created on Dec 7, 2016

@author: ToOro
'''
from _ast import arguments
"""note: insert, remove and sort that only modify list have no return value printed.
They return None. This is design principle for all mutable data structures in Python
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

# List comprehension
squares = [x**2 for x in range(10)] # The same as: map(lambda x: x**2, range(10))
# Complex list comprehension: combines the elements of two lists if they are not equal
## nested function
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

##
a1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
'''list comprehension above is the same as:
a1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            a1.append((x,y))
'''
vec = [-4, -2, 0, 2, 4]
[abs(x) for x in vec] # apply function for all the elements

## call method on each element
freshfruit = ['   banana', '   loganberry   ', 'passion fruit   ']
[weapon.strip() for weapon in freshfruit]

## create a list of 2-tuples (must be parenthesized) like (number, square)
[(x, x**2) for x in range(6)]

## flattern a list
vec1 = [[1,2,3], [4,5,6], [7,8,9]]
[num1 for element in vec1 for num1 in element]

## Matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
### zip() used in real-world
zip(*matrix)
### ordinary
transposed = [[row[i] for row in matrix] for i in range(4)] # transpose rows and columns
'''list comprehension above is equivalent to :
transposed = []
for i int range(4)
    transposed.append([row[i] for now in matrix])
    
and

for i in range(4)
    transposed_row = []
    for now in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
'''


