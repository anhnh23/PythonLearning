'''
Created on Dec 8, 2016

@author: ToOro
'''

"""dir()
used to find out which names a module defines, it returns a sorted list of strings
"""
# dir(argument)
import sys
dir(sys)

# dir() : lists the names you have defined currently (all types of names: variables, modules, function, etc)
# does not list the names of built-in functions and variables
dir()

# dir(builtin_argument) : list the names of builtin functions and variables
import __builtin__
print dir(__builtin__)