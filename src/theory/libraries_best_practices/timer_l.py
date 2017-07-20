'''
Created on Jul 20, 2017

@author: ToOro
'''
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
