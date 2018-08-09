'''Demonstrates working with lists'''

def demonstrate_lists():
    '''Just the simplest operations with lists.'''

    list_with_diverse_elements = ["Patti Smith", "Bruce Springsteen", 1978]
    print(list_with_diverse_elements[0])
    print(list_with_diverse_elements[-2:])

def demonstrate_list_methods():
    '''append(), insert(), del().'''
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
    # songs.remove(4)
    # print("A side:", songs)
