'''Demonstrates working with lists'''

def demonstrate_lists():
    '''Just the simplest operations with lists.'''

    list_with_diverse_elements = ["Patti Smith", "Bruce Springsteen", 1978]
    print(list_with_diverse_elements[0])
    print(list_with_diverse_elements[-2:])
    if list_with_diverse_elements == ["Patti Smith", "Bruce Springsteen", 1978]:                # comparing 2 lists
        print("list_with_diverse_elements = [\"Patti Smith\", \"Bruce Springsteen\", 1978]")
    else:
        print("list_with_diverse_elements = [\"Patti Smith\", \"Bruce Springsteen\", 1978]")

def demonstrate_list_methods():
    '''append(), insert(), remove(), pop(), extend().'''
    
    songs = ["Till Victory", "Space Monkey", "Because the Night"]
    print("Just the first three songs:", songs)
    songs.append("Babelogue")
    print("The first four songs:", songs)
    print("A side:", songs + ["Rock 'n' Roll Nigger"])
    print("There are still just four songs:", songs)
    songs.insert(3, "Ghost Dance")
    print("And now there are five songs:", songs)
    songs.insert(5, "Rock 'n' Roll Nigger")
    print("A side:", songs)
    songs.remove("Ghost Dance")
    print("After songs.remove(\"Ghost Dance\"):", songs)
    songs.pop()
    print("After songs.pop():", songs)
    songs.pop(1)
    print("After songs.pop():", songs)
    songs = ["Till Victory", "Space Monkey", "Because the Night"]
    print("Just the first three songs:", songs)
    songs.extend(['Ghost Dance', 'Babelogue', 'Rock \'n\' Roll Nigger'])
    print("After songs.extend(['Ghost Dance', 'Babelogue', 'Rock \'n\' Roll Nigger']) (A side):", songs)
