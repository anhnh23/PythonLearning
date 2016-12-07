'''
Python program is read by parser
Input to the parser is a stream of tokens, generated by the lexical analyzer.
This package describes how the lexical analyzer breaks a file into tokens.
SyntaxError is raised if the source cannot be decoded.
'''
# Explicit line joining with backslash character (\)
a, b = 0
if 1 < a < 10 \
    and 15 <= b <= 20:
    pass

# Implicit line joining is in parentheses
name = ['Ryan',
        'Nguyen']


'''NOTES:
1. Comment in the first or second line that matches coding[=:]\s*([-\w.]+) , this one is 
    processed as an encoding declaration. if no encoding declaration is found, the default
    encoding is UTF-8 (b'\xef\xbb\xbf')
'''