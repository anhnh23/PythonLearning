'''
Created on Jul 19, 2017

@author: ToOro
'''
from datetime import date

now = date.today()
birthday = date(1964, 7, 31)

age = now - birthday
print(age.days)