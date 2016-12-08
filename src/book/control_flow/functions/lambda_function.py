'''
Created on Dec 7, 2016

@author: ToOro
'''
"""
Use lambda keyword
Lambda function can reference variables from the containing scope
"""
# Return a function example
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
f(0) # => 42
f(1) # => 43

# Example: pass a small functions as an argument
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print (pairs) # => [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
