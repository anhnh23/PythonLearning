'''
Created on Jul 15, 2017

@author: ToOro
'''
import sys

# dir(): find out which names a module defines: variables, modules, functions, etc.
print(dir(sys))

#using dir() to list built-in functions and variables
#1st import builtins
import builtins
print(dir(builtins))