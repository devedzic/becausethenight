'''Demonstrates working with lists'''

def demonstrate_lists():
    '''Using just the simplest operations with lists.'''

    list_with_diverse_elements = ["Patti Smith", "Bruce Springsteen", 1978]                     # creating non-empty l.
    print(list_with_diverse_elements[0])                                                        # accessing elements
    print(list_with_diverse_elements[-2:])

    if list_with_diverse_elements == ["Patti Smith", "Bruce Springsteen", 1978]:                # comparing 2 lists
        print("list_with_diverse_elements = [\"Patti Smith\", \"Bruce Springsteen\", 1978]")
    else:
        print("list_with_diverse_elements = [\"Patti Smith\", \"Bruce Springsteen\", 1978]")

    list_with_diverse_elements = list_with_diverse_elements + ['NYC', 'Because the Night']      # concatenating 2 lists
    print('Concatenated list:', list_with_diverse_elements)
    print('Looping through the list elements:')

    for e in list_with_diverse_elements:                                                        # looping through a list
        print('\t', e)

def demonstrate_list_methods():
    '''Using append(), insert(), remove(), pop(), extend().
    count(), index(), reverse(), len(),... are not demonstrated here,
    but can be exercised in classes/labs as well.
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.'''

    songs = ["Till Victory", "Space Monkey", "Because the Night"]
    print("Just the first three songs:", songs)

    songs.append("Babelogue")                                               # append()
    print("The first four songs:", songs)
    print("A side:", songs + ["Rock 'n' Roll Nigger"])
    print("There are still just four songs:", songs)

    songs.insert(3, "Ghost Dance")                                          # insert()
    print("And now there are five songs:", songs)
    songs.insert(5, "Rock 'n' Roll Nigger")
    print("A side:", songs)

    songs.remove("Ghost Dance")                                             # remove()
    print("After songs.remove(\"Ghost Dance\"):", songs)

    songs.pop()                                                             # pop()
    print("After songs.pop():", songs)
    songs.pop(1)
    print("After songs.pop():", songs)

    songs = ["Till Victory", "Space Monkey", "Because the Night"]           # extend()
    print("Just the first three songs:", songs)
    songs.extend(['Ghost Dance', 'Babelogue', 'Rock \'n\' Roll Nigger'])
    print("After songs.extend(['Ghost Dance', 'Babelogue', 'Rock \'n\' Roll Nigger']) (A side):", songs)

def demonstrate_arrays():
    '''Using array.array() to build list-based numeric arrays.'''

    from array import array
    a = array('i', [1, -92, 3])                                             # 'i' - int; 'd' - double; etc.
    print('a:', a)
    print('a[1]:', a[1])

    b = [1, -92, 3]                                                         # lists and arrays are different types
    print('b:', b)
    print('b[1]:', b[1])

def populate_empty_list():
    '''Creating an empty list and populating it with random values.'''

    import random
    list_with_random_values = []                                            # create an empty list

    random.seed(234)                                                        # populate the list
    for i in range(1000):
        list_with_random_values.append(random.randint(1, 1000))
    print(list_with_random_values[:10], '...')
    print(str(list_with_random_values[:10]) + ',...')

def duplicate_list():
    '''Duplicating lists (carefully :))'''

    listA = [1, 2, 3]
    listB = listA                                           # NO!!! it only copies pointers/references!
    print('id(listA):',
          str(id(listA)) + '; id(listB):', id(listB))
    listB = listA + []                                      # this creates a new list, effectively the same as listA
    print('id(listA):',
          str(id(listA)) + '; id(listB):', id(listB))

def demonstrate_list_comprehension():
    '''Showing examples of list comprehension.'''

    from array import array
    a = array('i', [1, -92, 3])                                             # 'i' - int; 'd' - double; etc.
    print('a:', a)
    b = [str(x) for x in a]                                                 # list comprehension
    print('b:', b)
    print('join:', ''.join(b))                                              # make one big string from all b[i]
    print()

    songs = ["Till Victory", "Space Monkey", "Because the Night"]
    first_words = [x[0] for x in [y.split() for y in songs]]                # list comprehension
    print(first_words)
    print('join:', ''.join(first_words))                                    # make a big string from all first_words[i]
    print()
