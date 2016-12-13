'''
It is immutable
It can contain mutable object
'''

# we can declare a tuple as
t = 1234, 'hello', 2.3, 'c'

# nested tuple
t1 = t, (1, 2, 3) # t1 contains 2 tuples

# contains 2 tuples and 2 strings
t2 = t, 'eeee', 'ccc', (1, 2, 3)

# sequence unpacking
x, y, z, d = t # have to match the number of arguments
