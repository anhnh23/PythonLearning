"""There are 2 kinds of error:
+ Syntax errors (parsing error, ...)
+ Exceptions - errors detected during execution
"""

# using with keyword to clean-up in file manipulation
with open("file") as f: # no need to clean-up at finally
    for line in f:
        print line

# catch multi-exceptions
try:
    pass
except IOError as ioe: # alias for exception
    pass
except (RuntimeError, TypeError, NameError):
    pass
except: # catch all remaining exception
    raise # to re-raise an exception ('cause you don't want to handle this exception)
else: # if the try clause does not raise any exception (becareful - if the body could raise exception use try...catch)
    pass
finally: # clean-up
    pass

# the exception instance defines __str__() so the arguments can be printed directly
# without haveing to reference .args
try:
    raise Exception('spam', 'eggs') # to raise an exception
except Exception as inst:
    print type(inst) # the exception instance
    print inst.args # arguments stored in .args
    print inst # __str__ allows args to be printed directly
    x, y = inst.args
    print x, y
    
# User defined exception
class MyError(Exception):
    def __init__(self, value): # the default has been overridden
        self.value = value
    def __str__(self):
        return repr(self.value)
    
    
## 
try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value
    
## 
raise MyError('oops!')

# Create base exception example
class Error(Exception):
    """Base class for exceptions in this module"""
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    
    Attributes:
        expr -- input expression in which the error occurred
        msg -- explanation of the error
    """
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
        
class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.
    
    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg -- explanation of why the specific transition is not allowed
    """
    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg