'''This shows basic things during program with python
'''

""" Compiled Python files
Some tips:
+ When the Python interpreter is invoked with the -0 flag, optimized code is generated and
    stored in .pyo files. The optimizer currently doesn't help much; it only removes assert
    statements. When -0 is used, all bytecode is optimized; .pyc files are ignored and .py
    files are compiled to optimized bytecode.
+ Passing two -0 flags to the Python interpreter (-00) cause the bytecode compiler to perform
    optimizations that could in some rare cases result in malfunctioning programs. Currently
    only __doc__ strings are removed from the bytecode, resulting in more compact .pyo files.
+ A program doesn't run any faster when it is read from a .pyc or .pyo file than when it is read
    from a .py file; the only thing that's faster about .pyc or .pyo files is the speed
    with which they are loaded.
+ When a script is run by giving its name on the command line, the bytecode for the script
    is never written to a .pyc or .pyo file. Thus, the startup time of a script may be reduced
    by moving most of its code to a module and having a small bootstrap script that imports
    that module. It is also possible to name a .pyc or .pyo file directly on the command line.
+ It is possible to have called spam.pyc (or spam.pyo when -0 is used) without a file spam.py
    for the same module. This can be used to distribute a library of Python code in a form
    that is moderately hard to reverse engineer.
+ The module compileall can create .pyc files (or .pyo files when -0 is used) for all modules
    in a directory.
"""

"""CODING STYLE (VERY IMPORTANT)
1. use 4-space indentation, and no tabs.
2. Wrap lines (don't exceed 79 characters)
3. Use blank line to separate functions and classes, and larger blocks of code
    inside functions
4. When possible, put comments on a line of their own.
5. Use docstrings.
6. Use spaces around operators and after commas, but not directly 
    inside bracketing constructs: a = f(1, 2) + g(3, 4).
7. Name your classes and functions consistently; the convention is to use CamelCase
    for classes and lower_case_with_underscores for functions and methods.
    Always use <b>self</b> as the name for the <b>first method argument</b>.
8. Don't use fancy encodings if your code is meant to be used 
    in international environments. Plain ASCII works best in any way.
"""

""" ---------- Keywords and meaning
raise - to raise an exception
with - to alternative to the try/finally
def - declare a function
yeild - generator
"""

"""---------- Keywords and noting
else - also be used to do the false of 'while' and 'for' loop
pass - Python COMPOUNT STATEMENT (but not for def or class) cannot be empty (pass is used)
"""

""" ---------- Notes:
+ Flat is better than Nested
    - Using continue keyword is better than using nested loop.
+ Empty def or class statements: use a docstring, not pass
+ Functions:
    - They are objects (values)
    - They can also be keys into a dictionary
+ Assignment cannot occur inside expressions
"""

"""----------Unorganized
"""
#Lambda Example
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
high = 7
filter(lambda x, l=low, h=high: h>x>l, a_list)

#Lambda with local def
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
hight = 7
def within_bounds(value, l=low, h=hight):
    return h>value>l
filter(within_bounds, a_list)

"""Generator function
Syntax:
1. for avariable in somegenerator(arguments):
2. resulting_list = list(G(arguments)) <-- bounded generator

NOTES:
+ Generator is more flexible than functions
"""
#Example
def updown(N):
    for x in range(1, N):
        yield x
    for x in range(N, 0, -1):
        yield x
for i in updown(3): print(i) #prints: 1 2 3 2 1

#Generator works like build-in range, but return an iterator
step = 2
def frange(start, stop, stride=1.0):
    while start < stop:
        yield start
        start += step
        
#Recursion
"""
def rec(t):
    yield t[0]
    for i in (1,2):
        if t[i] is not None: yield from rec(t[i])
"""        

#Stack
def norec(t):
    stack = [t]
    while stack:
        t = stack.pop()
        yield t[0]
        for i in (2,1):
            if t[i] is not None: stack.append(t[i])
            

"""diference between import and from import
e.g. if import package.sub_package.sub_sub_package.module
whenever we use, we have to define the whole one (package.sub_package.sub_sub_package.module) 
    then call the funtions (in that module)
with from ... import module, we just need to define module.function
More about import:
+ from . import modules/functions : means from current package
+ from .. import modules/functions : means from parent
"""

"""Where to go beyond the basic
+ Python documentation: chills and trills
+ Python "recipes"
+ Python "idiomatic" coding
+ Work for free if necessary
    - Non profit
    - Open-source projects
"""