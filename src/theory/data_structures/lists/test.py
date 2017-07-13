'''
Created on Jul 13, 2017

@author: ToOro
'''
l = [1, 3, 2, 1, 3, 8 , 9]
print(l.index(3, 0, 5))
print(l.count(3))
l1 = l.copy()
l.sort(key=None, reverse=False)
print(l)
print(l1)
