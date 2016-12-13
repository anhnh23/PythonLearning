"""
Module is a file containing Python definitions and statements (with suffix .py)
The definitions you have made (functions and variables) are lost if you quit
    form the Python interpreter and enter it again
The definitions from a module can be imported into other modules or into the main module
    (via import keyword)
We can use a function often of a module by declare a variable contains module.function_name
    e.g. import fibo (in fibo has 2 functions fib and fib2) then some_name = fibo.fib
Module can contains executable statements as well as function definitions.
    Statements are intended to initialize the module
For efficiency reasons, each module is only imported once per interpreter session.
    Therefore, if changing modules, we must restart the interpreter 
    or use reload() (if just one)
Running modules as script: we have to define __name__ = "__main__" at the end of the module
    - to provide a convenient user interface to a module
    - for testing purposes
Cannot use >>> import module_name when it contains __name__ = "__main__" ('cause it is main file)
When a module is imported, the interpreter will do:
    1st. searches for a built-in module
    2nd. searches for a file name (named.py) in the list directories given by
        the variable sys.path:
        + the directory containing the input script (or the current directory).
        + PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH)
        + the installation-dependent default.
We can modify standard path by:
    import sys
    sys.path.append(...)
"""