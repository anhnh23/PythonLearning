'''
Created on Dec 8, 2016

@author: ToOro
'''
# can be chained
a = 3
b = 2
c = 1
d = 10
e = 9

if a < b == c < d >= e:
    pass

# assign the result of comparison
str1, str2, str3 = '', 'To', 'Tooo'
non_null = str1 or str2 or str3 # if the first one0 is empty, find the not next empty one
print non_null # result: To

# comparing sequences and other types
'''
use lexicographical ordering (thứ tự từ điển), if they differ this determines the outcome
    of the comparison (must have the same number of items)
'''
print (1,2,3) < (1,2,4)
print [1,2,3] < [1,2,4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1,2,3,4) < (1,2,4)
print (1,2) < (1,2,-1)
print (1,2,3) == (1.0, 2.0, 3.0)
print (1,2, ('aa', 'ab')) < (1,2,('abc', 'a'), 4)