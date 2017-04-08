'''
Created on Mar 23, 2017

@author: ToOro
'''
p = (4,5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data
_, shares, price, _ = data # only unpack shares and price

s = 'Hello'
a, b, c, d, e = s