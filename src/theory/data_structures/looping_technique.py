'''
Created on Jul 13, 2017

@author: ToOro
'''
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
#looping techniques: items() method
#looping through dictionary
for k, v in knights.items():
    print(k,v)
    
#looping through sequence
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# iteritems() : to get key and value at the same time
for k, v in knights.iteritems():
    print (k, v)
    
# loop over 2 or more sequences
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? It is {1}.'.format(q, a))
    
# loop in reverse
for i in reversed(range(1, 10, 2)):
    print(i)