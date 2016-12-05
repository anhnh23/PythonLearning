'''
Syntax:
def function-name(parameters):
    statement(s)

Explaination:
+ parameter - can be indentifier=expression
 
'''

# be keys into a dictionary
dic = {'a':10, 'b':20, 'c':30}
inverse = {}
for f in list(dic):
    inverse[dic[f]] = f
    
print(dic)
print(inverse)

"""This is case parameter is indentifier=expression, saving a reference's value
known as the default value for the parameter.
"""
def f(x, y=[]): 
    y.append(x)
    return y
   
print(f(1))
print(f(2))

# alter the default value of y
def f1(x, y=None):
    if y is None: y = []
    y.append(x)
    return y

print(f1(1))
print(f1(2))

""" ---------- *args and **kwds
*args - any extra positional arguments to a call will be collected in a (possibly empty)
    tuple and bound in the call namespace to the name args
**kwds - any extra named arguments will be collected in a (possible empty) dictionary
    whose items are the names and values of those arguments, and bound to the name kwds
    in the function call namespace
"""
#Examples
def sum_args(*numbers):
    return sum(numbers)
print('Sum 5 + 7 is : ', sum_args(5, 7))

"""---------- Keyword-only parameter
should come after *args (if any) and before **kwargs (if any)
"""
#Examples
def f_kwonly(a, *, b, c=56): # b anc c are keyword-only
    return a, b, c

f_kwonly(12, b=34) #returns (12, 34, 56) - c's optional, having a default
f_kwonly(12) # raises a TypeError exception
    