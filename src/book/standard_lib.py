'''
Created on Dec 9, 2016

@author: ToOro
'''
# OS
import os # for interacting with the operating system
## common functions
os.getcwd() # return the current working directory
os.chdir('path') # change current working directory 
os.system('command') # run the command
dir(os) # returns a list of all module functions
help(os) # returns an extensive manual page created from the module's docstrings

##
import shutil # for daily file and directory management tasks
shutil.copyfile('src', 'dst')
shutil.move('src', 'dst')

# File wildcards
import glob # for making file lists from directory wildcard searches
glob.glob('*.py')

# command line arguments
import sys # stores arguments

import getopt # stores options
getopt.getopt('args', 'shortopts', 'longopts')

import argparse # command line processing

# Error Output Redirection and Program Termination
sys.stderr
sys.exit()

# String pattern matching
import re # regualar expression
re.findall('pattern', 'string', 'flags')
re.sub('pattern', 'repl', 'string', 'count', 'flags')

# Mathematics
import math
math.cos(math.pi/4.0)
math.log(1024,2)

import random
random.choice(['apple', 'pear', 'banana'])
random.sample(xrange(100), 10) # sampling without replacement
random.random() # random float
random.randrange(6) # random integer chosen from range(6)

# Internet
import urllib2 # for retrieving data
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line: # look for Eastern Time
        print line
        
import smtplib, poplib # for just sending and receiving mail, we need a mail server
server = smtplib.SMTP('localhost')
server.sendmail('from', 'to')
server.quit()

# Dates and Times
from datetime import date # the focus of the implementation is on efficient member extraction
now = date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
## supports calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days

# Data compression
import zlib, gzip, bz2, zipfile, tarfile # for compression
s = 'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s) # <--
len(t) # will be different
zlib.decompress(t)
zlib.crc32(s) # crc 32 checksum of string

# Performance Measurement
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1;b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()

import profile, pstats # for identifying time critical section in large blocks of code

# Quality Control
import doctest # for scanning a module and validating tests embedded in a program's docstring.
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>> print average([20, 20, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)
doctest.testmod() # automatically validate the embedded tests

import unittest # more comprehensive set of tests to be maintained in a separate file
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
            
unittest.main() # calling from the command line invokes all tests

# Batteries Included
import xmlrpclib, SimpleXMLRPCServer # make implementing remote procedure calls into an almost trivial task.
import email # for managing email message, including MIME and other RFC 2822-based message doc.
    # has a complete toolset for building  or decoding complex message structure (including
    # attachments) and for implementing internet encoding and header protocols.

## Two modules/packages below greatly simplify data interchange between Python applications and other tools 
import xml.dom, xml.sax # for parsing this popular data interchange format.
import csv # supports direct reads and writes in a common database format.

import gettext, locale, codecs # for internationalization 

# Output Formatting
import repr # provides a version of repr() CUSTOMIZED for abbreviated displays of large or
    # deeply nested containers
repr.repr(set('superasofasfaosdfa'))

import pprint # offers more sophisticated control over printing both buil-in and user defined objects
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30) # when result is longer than one line, line breaks and indentation are added
"""
Result
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
"""

import textwrap # formats paragraphs of text to fit a given screen width
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
textwrap.fill(doc, width=40)

import locale # accesses a database of culture specific data formats
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv() # get mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)
locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), 
    grouping=True) #result '$1,234,567.80'

# templating
from string import Template
## placeholder $ identifies alphanumeric characters and underscores.
## $$ create a single escaped $
t = Template('${village}folk send $$10 to $cause.')
## substitute() raises a KeyError when a placeholder is not supplied in a dictionary or a 
## key argument.
t.substitute(village='Nottingham', cause='the ditch fund')
## result: 'Nottinghamfolk send $10 to the ditch fund.'

## safe_substitute() leaves placeholders unchanged if data is missing
t = Template('Return the $item to $owner')
d = dict(item='unladen swallow')
t.substitute(d) # error occurs
t.safe_substitute(d) # this one is fine

## template subclasses can specify a custom delimiter
## batch renaming utility for a photo browser may elect to use percent signs for placeholders
## such as the current date, image sequence number, or file format
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print '{0} --> {1}'.format(filename, newname)
""" Result:
img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
"""

# Binary Data Record Layouts
import struct # pack(), unpack() for working with variable length binary record formats
## loop through header information in a ZIP file without using the zipfile module.
## 'H' and 'I' represent two and four byte unsigned numbers
## '<' indicates stardard size and in little-endian byte order
data = open('myfile.zip', 'rb').read()
start = 0
for i in range(3): #show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
    
    start += 16
    filename = data[start:start + filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print filename, hex(crc32), comp_size, uncomp_size
    
    start += extra_size + comp_size # skip to the next header
    
# Multi-threading
import threading # for multi-threading programming
import zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
        
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print 'Finished background zip of: ', self.infile
        
background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print 'The main program continues to run in foreground'

background.join() # wait for the background task to finish
print 'Main program waited until background was done.'

## Queue.Queue objects for inter-thread communication and coordination are easier to design
## more readable, and more reliable
