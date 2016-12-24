'''
Created on Dec 22, 2016

@author: ToOro
'''
"""
Regular expression operations - https://docs.python.org/3.5/library/re.html#re-syntax
"""
import re, regex

p = re.compile(r'(?<=John\s)McLane')
results = p.finditer('John goes to the market with John McLane')
for result in results:
    print(result.start(), result.end())