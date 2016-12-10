'''
Created on Dec 4, 2016

@author: ToOro
'''
import math

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

# zfill()
'12'.zfill(5) #result is: '00012'

# format()
print 'we are the {} who say "{}!"'.format('knights', 'Ni')

for x in range(1, 11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
    
# index and keyword (keyword have to come after)
print '{0} and {1}'.format('spam', 'egg')
print '{1} and {0}'.format('spam', 'egg')
print '{food1} and {food2}'.format(food1='spam', food2='egg')
print '{food} and {0}'.format('egg', food='spam') # keyword have to come after

"""
Convert value before it is formatted
'!s' apply str()
'!r' apply repr()
"""
print 'The value of PI is {!r}'.format(math.pi)

# using ':'
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone) # key (name) and value (phone)
'''result:
Dcab      ==>      7678
Jack      ==>      4098
Sjoerd    ==>      4127
'''
    
# format by name
print ('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)) # if no need to split up

# format with keyword
print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

# format with %
print 'The value of PI is %5.3f' % math.pi
