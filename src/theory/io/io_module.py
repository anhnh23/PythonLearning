#str() returns representations of value which are fairly human-readable
#repr() generate representation which can be read by the interpreter
s = 'Hello,\n world.'
print(str(s))
print(repr(s))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
'''str()
    1. rjust right justifies
    2. ljust left ----------
    3. center
    4. zfill: pads a numeric string on the left with zeros
    '''

#format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

'''
    !a : ascii
    !s : apply str()
    !r : repr()
    '''
contents = 'eels'
print('My hovercraft is full of {!r}.'.format(contents))

# built-in function vars() supports
## --- Math
import math
## using ":"
print('The value of PI is approximately {:.3f}.'.format(math.pi))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
## ---
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
## ---
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
## Using **
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
## using %
print('The value of PI is approximately %5.3f.' % math.pi)

###########################
# --- File Integration ---#
###########################
''' open(filename, mode) returns a file object
    a: append
    r+: read and write
    b: open in binary mode
'''
f = open('workfile', 'w')

'''Ending line
    \n: on Unix
    \r\n: on Windows
'''

"""Default close file with "with" keyword"""
with open('workfile') as f:
    read_data = f.read()
    
#Loop over file
for line in f:
    print(line, end='')
    
################
# --- JSON --- #
################
import json
# dump(x, f) serializes the object to a text file; f: text file.  
json.dumps([1, 'simple', 'list'])
# load decodes object
json.load(f)