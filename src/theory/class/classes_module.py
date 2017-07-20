'''
Created on Jul 19, 2017

@author: ToOro
'''
# Name mangling
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
            
    __update = update # private copy of original update() method
    
class MappingSubclass(Mapping):
    def update(self, keys, values):
        #provides new signatures for update()
        #but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
            
class Employee:
    pass

john = Employee()
john.name = 'John'
john.dept = 'Computer Lab'
john.salary = 1000

# demonstrates iter()
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
    
rev = Reverse('spam')
for char in rev:
    print(char)
    
'''Generation: creating iterators
    yield: to return data (each time next() is called on it, the generator resumse
        where it left off (it remembers all the data values and which statement was last executed)
'''
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
for char in reverse('golf'):
    print(char)
    
'''Generator expressions'''
sum(i*i for i in range(10))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

unique_words = set(word for line in page for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

