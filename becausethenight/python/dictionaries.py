"""Demonstrates dictionaries
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary
- the local variables in a function - stored in a dictionary
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    """

    blank_dictionary = {}                                       # create a blank (empty) dictionary
    print('blank_dictionary:', blank_dictionary)
    blank_dictionary['album'] = 'Easter'
    print('blank_dictionary with added item:', blank_dictionary)
    print()
                                                                # create a non-empty dictionary
    because_the_night = {'author_1': 'Bruce Springsteen',
                         'author_2': 'Patti Smith',
                         'song': 'Because the Night'
    }
                                                                # print a non-empty dictionary
    print('Dictionary because_the_night:', because_the_night)
    print('items():', because_the_night.items())                # print all items using the items() function
    print('Dictionary because_the_night, item by item:')        # print one item per line
    for k, v in because_the_night.items():
        print(k + ': ', v)
    print()

    from pprint import pprint                                   # pprint dictionary in one column
    pprint(because_the_night, width=1)
    print()
                                                                # using keys() and values() functions
    print(because_the_night.keys())
    print(because_the_night.values())
    print(list(because_the_night.keys()))
    print(list(because_the_night.values()))
    print()

    print('author_1:', because_the_night['author_1'])
    # print('items()[0]:', because_the_night.items()[0])          # doesn't work, must be list()-ed first
    print('items()[0]:', list(because_the_night.items())[0])
    print('Key in items()[0]:', list(because_the_night.items())[0][0])
    print()

    because_the_night['album'] = 'Easter'
    print('New key-value pair added:', because_the_night)
    del because_the_night['song']
    print('The "song" key-value pair deleted:', because_the_night)
    print()

    # from pprint import pprint
    # pprint(because_the_night)
    # print(because_the_night)
    # pprint(because_the_night.items())
    # print(because_the_night.items())


def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    """

    if by == 'k':
        d_sorted = sorted(zip(d.keys(), d.values()))
    elif by == 'v':
        d_sorted = sorted(zip(d.values(), d.keys()))
    else:
        return None
    # Alternative 1:
    # from operator import itemgetter
    # if by == 'k':
    #     d_sorted = sorted(d.items(), key=itemgetter(0))
    # elif by == 'v':
    #     d_sorted = sorted(d.items(), key=itemgetter(1))
    # else:
    #     return None
    # Alternative 2:
    # if by == 'k':
    #     d_sorted = sorted(d.items(), key=lambda item:item[0])
    # elif by == 'v':
    #     d_sorted = sorted(d.items(), key=lambda item:item[1])
    # else:
    #     return None
    return dict(d_sorted)                                         # d_sorted is a list, dict(d_sorted) is a dictionary


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    because_the_night = {'author_1': 'Bruce Springsteen',
                         'author_2': 'Patti Smith',
                         'song': 'Because the Night'
    }

    print('Sorting by keys:', sort_dictionary(because_the_night, 'k'))
    print('Sorting by values:', sort_dictionary(because_the_night, 'v'))
    print('Sorting by whatever else:', sort_dictionary(because_the_night, 1))
