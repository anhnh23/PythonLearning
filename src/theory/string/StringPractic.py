'''
Created on Jul 8, 2017

@author: ToOro
'''
print(3* 'un' + 'ium')

word='Python'
print(len(word))

squares = [1, 4, 9, 16, 25]
print(squares[:])

squares += [30, 35, 40]
print(squares[:])

x = int(input("Please enter an integer: "))

if x < 0:
    x=0;
    print('Negative changed to zero')
else:
    print('More')