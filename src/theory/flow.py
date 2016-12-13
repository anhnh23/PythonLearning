'''
Created on Dec 4, 2016

@author: ToOro
'''

'''----------NOTES----------
1. Don't alter mutable objects while looping on them
2. When looping on a list, do not insert, append, or delete items
    (rebinding an item at an existing index is OK).
3. When looping on a dictionary, do not add or delete items
    (rebinding the value for an existing key is OK).
4. When looping on a set, do NOT ADD or DELETE items
    (no alteration permitted).
'''
#Initalizing
someseq = range(10)
d={'a': 10, 'b': 20} # dictionary
""" ------------ FOR SECTIION------------------------
Syntax:
for target in iterable:
    statement(s)
"""
# Normal use
for letter in 'ciao':
    print('give me a', letter, '...')
    
# if iterable is a dictionary
for key, value in d.items():
    if key and value:
        print(key, value)
    
# variable is still exist at the last processing
def process(arg):
    print(arg)

for x in someseq:
    process(x)
print('Last item processed was', x) # x=4 is still exist

""" ---------- List Comprehension
Syntax:
[expression for target in interable lc-clauses]
"""
# Example 1
result1 = [x+1 for x in someseq]

result2 = []
for x in someseq:
    result2.append(x+1)
    
result3 = [x+1 for x in someseq if x > 2]
print(result3)