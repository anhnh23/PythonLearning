'''
Created on Jul 13, 2017

@author: ToOro
'''
def make_incrementor(n):
    return lambda x: x + n

f=make_incrementor(42)

print(f(0))
print(f(1))