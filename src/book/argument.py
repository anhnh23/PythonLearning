'''
Created on Dec 7, 2016

@author: ToOro
'''
'''Default argument is a mutable object'''
#Example
def f(a, L=[]):
    L.append(a)
    return L

print f(1) # => [1]
print f(2) # => [1, 2]
print f(3) # => [1, 2, 3]

# don't want the default to be shared
def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
        
# *args and **keywords
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# arbitrary argument list
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
    
# Unpacking argument list
##--- * operator
args = [3,6]
print range(*args) # => [3, 4, 5] 

##--- ** operator
def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"
    
d = {"voltage": "four million", "state":"bleeding' demised", "action": "VOOM"}
parrot(**d)