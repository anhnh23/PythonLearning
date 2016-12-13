"""
3.3. Special method names; operator overloading (allow classes to define their own behavior)
3.3.1. Basic customization
    object.__new__ : new instance
    object.__init__ : customize the instance, called after the instance has been created, but before it is return to the caller.
    object.__del__ : called when the instance is about to be destroyed.
        NOTE: 
            + del x # x.__del__()
    object.__repr__ : compute the "official" string representation of an object.
    object.__str__ 
    object.__bytes__
    object.__format__
    object.__lt|le|eq|ne|gt|ge__ : rich comparison
    object.__hash__
    object.__bool__ : True / False
    
3.3.2. Customizing attributes access
    object.__getattr__ : called when an attribute lookup has no found the attribute in the usual places
    object.__getattribute__ : called unconditionally to implement attribute accesses for instance of the class
    object.__setattr__
    object.__delattr__
    object.__dir__ : called when dir() is called on the object
3.3.2.1. Implementing Descriptors
    object.__get__ : get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access).
    object.__set__ : set the attribute on an instance instance of the owner class to a new value. 
    object.__delete__ :
    
3.3.3.5. Metaclass
"""
#Example: using an collections.OrderedDict to remember the order that class variables are defined
class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()
    
    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        
class A(metaclass=OrderedClass):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass
    
A.members('__module__', 'one', 'two', 'three', 'four')
"""
3.3.5. Emulating callable objects

"""