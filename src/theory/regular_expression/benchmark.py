'''
Created on Dec 23, 2016

@author: ToOro
'''
import re
from time import clock as now
import cProfile

def test(f, *args, **kargs):
    start = now()
    f(*args, **kargs)
    print("The function %s lasted: %f" %(f.__name__, now() - start))
    
    
# Test regular expression
def alternation(text, debug=False):
    if debug:
        pat = re.compile('spa(in|niard)', re.DEBUG)
    else:
        pat = re.compile('spa(in|niard)')
    pat.search(text)
    
# if it match, it is very fast (if not so slow 'cause start over and over again)
## The problem below is not matched c
def catastrophic(n):
    print("Testing with %d characters" %n)
    pat = re.compile('(a+)+c')
    text = "%s" %('a' * n)
    pat.search(text)
    
## Added c to make it matched
def non_catastrophic(n):
    print("Testing with %d characters" %n)
    pat = re.compile('(a+)+c')
    text = 'a' * n
    text += 'c'
    pat.search(text)
# 1st - Using test function
#test(alternation, "spain")

# 2nd - Using cProfile
#cProfile.run("alternation('spaniard')")

# 3rd - Using DEBUG mode of re
#test(alternation, "spain", debug=True)

for n in range(20, 30):
    #test(catastrophic, n) # this one is so slow when a increase
    test(non_catastrophic(n)) # this one is very ideal





