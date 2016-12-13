'''
Created on Dec 8, 2016

@author: ToOro
'''
"""
Set supports mathematical operations like: union, intersection, difference, and symmetric difference
Set is unordered collection with no duplicate elements.
Creating set:
1. {elements}
2. create an empty set: use set(), not {}
3. make set from a collection, set(collection)
"""
#1.
a1 = {2, 3, 5, 7, 21, 11, 2, 5, 15, 7}

#3. 
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
## make set
fruit = set(basket)

#Others
## fast membership testing
'orange' in fruit

## Remove all duplicate letters
a = set('absfwersakiwlsldfkow')
b = set('asweroiqwerqlfasoiqwperjqw;ajfo')

## mathematical operations
a - b # in a not in b
a | b # in either a and b
a & b # in both a and b
a ^ b # in a or b (not both)

## set comprehension
a2 = {x for x in 'asdwroafaqwerasdf' if x not in 'abc'}
