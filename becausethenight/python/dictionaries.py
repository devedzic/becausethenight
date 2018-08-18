'''Demonstrates dictionaries'''


def demonstrate_dictionaries():
    '''Creating and using dictionaries.'''

    because_the_night = {'author_1': 'Bruce Springsteen',
                         'author_2': 'Patti Smith',
                         'song': 'Because the Night'
    }
    print('Dictionary because_the_night:', because_the_night)
    print('items():', because_the_night.items())
    print('Dictionary because_the_night, item by item:')
    for k, v in because_the_night.items():
        print(k + ': ', v)
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

    blank_dictionary = {}                                       # create a blank (empty) dictionary
    print('blank_dictionary:', blank_dictionary)
    blank_dictionary['album'] = 'Easter'
    print('blank_dictionary with added item:', blank_dictionary)
    print()

    # from pprint import pprint
    # pprint(because_the_night)
    # print(because_the_night)
    # pprint(because_the_night.items())
    # print(because_the_night.items())
