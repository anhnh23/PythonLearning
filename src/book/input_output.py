'''
Created on Dec 8, 2016

@author: ToOro
'''
"""
There are 3 ways to write values:
1. expression statements
2. print statement
3. write() method - should convert to string first

repr() or str() functions : to convert any value to a string
repr() of a string adds string quotes (backslashes will be kept if any)
"""
s = 'hello, world'
str(s)
repr(s)

str(1.0/7.0)
repr(1.0/7.0)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'

hello = 'hello, \nworld'
hellor = repr(hello)
print hellor

hellos = str(hello)
print hellos

# The argument to reprs() may be any Python object
repr((x, y, ('spam', 'egg')))

# write table with repr() and normal way
## repr() (rjust is right-justify
for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    # note trailing comma on previous line
    print repr(x*x*x).rjust(4)
    
## normal
for x in range(1, 11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
    
    
# file manipulation
## open(filename, mode)
### mode: r: read, w: write & replace, a: append, r+: read and write
### mode for Widows: b: append, r, w, r+ same as above
f = open('workfile', 'w') # w: write (replace the existing one)

# read()
f.read() # read file, if EOF '' will be returned

# readline() : contain \n to indicate end of line
f.readline() #result: 'content...\n' 

# use loop to read line
for line in f: # memory efficient, fast and leads to simple code
    print line
    
# how to read all lines at a time
list(f) and f.readlines()

f.write('something') # will return None

# tell() returns a integer giving file object's current position in the file
# seek(offset, from_what) to change the object's position
f.seek(5) # go to the 6th byte in the file
f.seek(-3, 2) # go to the 3rd byte before the end - reverse seeking

"""with keyword
with keyword is the good practice when dealing with file object (properly closed after
    its suite finishes, even if an exception is raised.
"""
with open('workfile', 'r') as f:
    read_data = f.read()

# isatty() and truncate() will be explored later

"""JSON
json.dumps([1, 'simple', 'list']) - view JSON string representation
json.dump(x, f) - serializing object x to file with json format
json.load(f) - de-serializing the serialized object.
"""

"""pickle
Contrary to JSON, pickle is a protocol which allows the serialization of arbitrary complex
    Python objects.
"""

