'''
Created on Dec 8, 2016

@author: ToOro
'''
"""
Behind the scene: for statement calls iter() on the container object.
"""
#--------- How iter() works ---------
s = 'abc'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))

# enumerate() : can be retrieved index and corresponding value
for i, v in enumerate(['tic', 'tac', 'toe']):
    print (i, v) # result: 0 tic \n 1 tac \n 2 toe
    
# zip() : to loop over 2 or MORE sequence at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print ('What is your {0}? It is {1}.'.format(q, a))
    
# loop in reversing
for i in reversed(range(1, 10, 2)):
    print (i)
    
# loop and sort
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)): # firstly eliminate duplicated elements with set, then sort
    print (f)
    
# iteritems() : to get key and value at the same time
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print (k, v)
    
# filter data
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

words=['cat','window', 'defenestrate']
for w in words:
    print(w, len(w))
    
for element in (1,2,3):
    print(element)
    
for key in {'one':1, 'two':2}:
    print(key)
    
for char in "123":
    print(char)
    
for line in open("myfile.txt"):
    print(line, end='')

    
