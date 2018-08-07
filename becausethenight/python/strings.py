# Demonstrates working with strings

import string


def demonstrate_formatting():

    print("%7.3f, %5s" % (4/3, 'ee'))
    print('I love \t\t\'Because the Night\'')
    print('C:\never')                               # \n is the new line char
    print(r'C:\never')                              # r'...' - raw formatting
    print()
                                                    # using """...""" for multi-line formatting
    print("""Patti Smith's songs:
                - Because the Night
                - Till Victory
                - ...
    """)
    print()

    # print('ddddd' 'hhhhh')                        # works for string literals
    # print('ddddd', 'hhhhh')
    # print()

    print("Patti Smith     " * 3)                   # string "multiplication"
    print("Patti Smith's " + str(1) + "st album")   # str(<numeric>) and the like MUST be used in concatenation
    print()

    patti = "Patti Smith"
    print(patti)
    print(patti[3:5])                               # substrings / slicing
    print(patti[:3])
    print(patti[-5:])
    print(patti[:])
    print()

    print(string.whitespace)
    print(str(string.whitespace))                   # str() and repr() usually give the same results, and usually str()
    print(repr(string.whitespace))                  # is used; but, with e.g. whitespace chars, there is a difference
    print()

def demonstrate_fancy_formatting():
    patti = "Patti Smith"
    # print('{0}, {1}, {2}'.format(patti, ': ', "Because the Night"))
    # print('{0} {1} {2}'.format(patti, ':', "Because the Night"))
    print('{0}{1} {2}'.format(patti, ':', "Because the Night"))
    print('{0}{1} {2}, {3}'.format(patti, ':', "Because the Night", 1978))

def demonstrate_string_operations():
    song = 'Because the Night'
    if song.endswith('Night'):
        print('Because the Night ends with \'Night\'')
    else:
        print('Because the Night doesn\'t end with \'Night\'')
    print('split():', song.split())
    print('center():', song.center(50, '*'))
    if 'Because' in song:                           # no contains() as in Java String, this is how to check for it
        print('\'Because\' is in \'Because the Night\'')
    else:
        print('\'Because\' is in \'Because the Night\'')
    if song == 'Because the Night':                 # no equals(), this is how to compare strings for equal content
        print('The song is \'Because the Night\'')
    else:
        print('The song is not \'Because the Night\'')
    print('len():', len(song))
    # ...

