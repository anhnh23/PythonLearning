'''
Created on Jul 13, 2017

@author: ToOro
'''
# List comprehension
# The same as: map(lambda x: x**2, range(10))
squares = [x**2 for x in range(10)]
# Complex list comprehension: combines the elements of two lists if they are not equal
## nested function
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

#-------------------------------------------------------------
a1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            a1.append((x,y))
# ==
a1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#-------------------------------------------------------------

vec = [-4, -2, 0, 2, 4]
[abs(x) for x in vec] # apply function for all the elements

## call method on each element
freshfruit = ['   banana', '   loganberry   ', 'passion fruit   ']
[weapon.strip() for weapon in freshfruit]

## create a list of 2-tuples (must be parenthesized) like (number, square)
[(x, x**2) for x in range(6)]

## flattern a list using listcomp with two 'for'
vec1 = [[1,2,3], [4,5,6], [7,8,9]]
[num1 for element in vec1 for num1 in element]

## Matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
### zip() used in real-world

### ordinary

# ---------------- transpose rows and columns------------------
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
# ==
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
# ==
transposed = [[row[i] for row in matrix] for i in range(4)]
# ==
list(zip(*matrix))
# --------------------------------------------------------------