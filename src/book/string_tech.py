'''
Created on Dec 4, 2016

@author: ToOro
'''
print "hello"
words = "hello"
for w in words:
    print w
    
# print string with indentation
def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

print my_function.__doc__ # remember there is no ()