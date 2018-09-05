'''Demonstrates peculiarities of if, for, while and other statements'''


def demonstrate_branching():
    '''Details and peculiarities of if statements.'''

    because_the_night = 'Because the Night'
    because_the_Night = 'Because the Night'                 # id()'s are the same for equal strings!
                                                            # (but not for lists, user class instances,...)
                                                            # (not even for strings if this is run in Python console!)
    print('because_the_night:', because_the_night + '; id(because_the_night):', id(because_the_night))
    print('because_the_Night:', because_the_Night + '; id(because_the_Night):', id(because_the_Night))
    print()

    if because_the_night:                                   # not necessarily a boolean!
        print(because_the_night)
    else:
        print(None)
    print()

    if because_the_night is 'Because the Night':            # this is True for strings!
        print('because_the_night is because_the_Night')
    elif because_the_night == because_the_Night:            # there can be more elif's;
        print('because_the_night == because_the_Night')     # no switch in Python, elif's are like case's
    else:
        print('Neither == nor is...')
    print()

    because_the_night_l1 = ['Because the Night']
    because_the_night_l2 = ['Because the Night']
    if because_the_night_l1 is because_the_night_l2:            # this is False for lists etc.!
        print('because_the_night_l1 is because_the_night_l2')
    elif because_the_night_l1 == because_the_night_l2:          # this is True, == compares contents
        print('because_the_night_l1 == because_the_night_l2')
    else:
        print('Neither is, nor == ...')
    print()


def demonstrate_loops():
    '''Different kinds of loops. Also break and continue.'''

    songs = ["Till Victory", "Space Monkey", "Because the Night", "Rock 'n' Roll Nigger", "Ghost Dance"]

    for song in songs[:2]:
        print(song, ',', len(song), 'chars')
    print()

    for song in [songs[2], songs[4], songs[0]]:
        print(song, ',', len(song), 'chars')
    print()

    for i in range(10, 0, -1):                      # step in range()
        print(i, end=' ')
    print()
    print()

    for _ in range(10):                             # unimportant counter
        print("Hi :)")
    print()

    for i, song in enumerate(songs):                # enumerate()
        print(str(i+1) + ':', song)
    print()

    other_songs = ["Till Victory",
                   "Space Monkey",
                   "Rock 'n' Roll Nigger",
                   "Ghost Dance"]
    for song in songs:
        if song in other_songs:
            continue                                # continue
        print(song)
    # Alternatively
    # selected_songs = [song for song in songs if song not in other_songs]
    # print(', '.join(selected_songs))
    print()

    # for song in songs:
    #     if song == "Rock 'n' Roll Nigger":
    #         break                                   # break
    #     print(song)
    # print()
    #
    # i = 0                                           # while loop
    # while songs[i] != 'Because the Night':
    #     print(songs[i])
    #     i += 1
    # print()

