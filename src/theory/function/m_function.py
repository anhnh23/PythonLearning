'''
Created on Jul 12, 2017

@author: ToOro
'''
args = [2,5]
print(list(range(*args)))

def methods(a, b='bbb', c='ccc'):
    print("inside")
    
d={"a": "aaa", "b":"BBB", "c":"CCC"}
methods(**d)