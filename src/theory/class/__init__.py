class Dog:
    kind = 'canine' # class variable shared by all instances
    def __init__(self, name):
        self.name = name # instance variable unique to each instance
        
d = Dog('Fido')
e = Dog('Buddy')

d.kind # => canine
e.kind # => canine
d.name # => Fido
e.name # => Buddy

#-----------
class Dog1:
    tricks = [] # mistaken use of a class varible
    def __init__(self, name):
        self.name = name
        
    def add_trick(self, trick):
        self.tricks.append(trick)
        
d = Dog1('Fido')
e = Dog1('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks # => ['roll over', 'play dead'], unexpected

# Correct is:
class Dog2:
    def __init__(self, name):
        self.name = name
        self.tricks = []
        
    def add_trick(self, trick):
        self.tricks.append(trick)
    
d = Dog2('Fido')
e = Dog2('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

d.tricks # => 'roll over'
e.tricks # => 'play dead'

# private variable and class-local reference
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
            
    __update = update # private copy of original update() method
    
class MappingSubclass(Mapping): #inheritance
    def update(self, keys, values):
        #provides new signature for update(), but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
# odds and ends
class Employee:
    pass

john = Employee() # create an empty employee record

#Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# iter()
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init___(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
rev = Reverse('spam')
iter(rev) # ==> print an object
## to get a correct result
for char in rev:
    print(char)
    
# yield keyword: Generators are a simple and power tool for creating iterators.
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
for char in reverse('golf'):
    print(char)
    
# generator expressions use () instead of [] (list comprehension)
sum(i*i for i in range(10)) # sum of squares

##read two lists
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x, y in zip(xvec, yvec)) # dot product

##
from math import pi, sin
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91))

##
page = []
unique_words = set(word for line in page for word in line.split())

## highest student
graduates = []
valeictorian = max((student.gpa, student.name) for student in graduates)

##
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

