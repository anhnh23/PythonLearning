'''
Created on Dec 4, 2016
This shows all (learnt) cases for using dictionaries.
@author: ToOro
'''
# declaration
tel = {'jack': 4098, 'sape': 4139}

#dictionary is mutable object
tel['jack'] = 4000

#adding new element
tel['guido'] = 4444

#delete an element
del tel['jack']

#show all keys in dictionary
tel.keys()

# check key in dictionary
'guido' in tel

# build a dictionary from sequence
tel1 = dict([('sape', 4224), ('guido', 2222), ('jack', 4000)])
## or
tel2 = dict(sape=4139, guido=2222, jack=4000)

# dict comprehension
d = {n:n//2 for n in range(10)} #result:  {0:0, 1:0, 2:1, 3:1, ...
