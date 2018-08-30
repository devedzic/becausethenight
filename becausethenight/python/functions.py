'''Demonstrates details of writing Python functions: annotations, default args, kwargs'''


def demonstrate_annotations(artist: str, song: str = 'Because the Night') -> str:
    '''Demonstrates how to use annotations of function parameters/arguments and of function return type.'''

    print("Annotations:", demonstrate_annotations.__annotations__)
    print(r'Parameters/Arguments:', 'artist:', artist + ',', 'song:', song)
    return artist + ', ' + song

def show_song(artist, song ='Because the Night', duration = 180):
    '''Demonstrates default arguments/parameters'''

    print(artist, end=': ')
    print(song, end=', ')
    print(duration)
    print()

def use_flexible_arg_list(prompt: str, *songs):
    '''Demonstrates flexible number of arguments/parameters'''

    # songs = list(songs)                                   # not necessary, although improves readability
    print(prompt + ': ', end='')
    for song in songs:
        print(song, end=', ')
    print('...')
    print()

def use_all_categories_of_args(prompt, *albums, song = 'Because the Night', **authors):
    '''Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).'''

    print(prompt + ': ', end='')
    if len(albums) != 0:
        print('Album(s):', end=' ')
        for album in albums:
            print(album, end='')
            if album != albums[-1]:                         # if it's not the last album in albums
                print(', ', end='')
            else:
                print('; ', end='')
        print('Song:', song, end='')
    else:
        print(song)
    if authors != {}:
        print('; Author(s):', end=' ')
        for key in authors:
            print(authors[key], end='')
            if key != list(authors.keys())[-1]:             # if it's not the last author
                print(', ', end='')
            else:
                print()
    print()


if __name__ == "__main__":

    demonstration = demonstrate_annotations('Patti Smith', 'Because the Night')
    print(demonstration)
    print()

    f = demonstrate_annotations                     # rename a function (general renaming mechanism)
    f('Patti Smith', 'Because the Night')
    print()

    show_song('Patti Smith')                        # working with default parameters/arguments
    show_song('Patti Smith', duration=234)
    show_song('Patti Smith', song='Babelogue')
    show_song('Patti Smith', 'Babelogue', 123)
    show_song('Patti Smith', 123)
    show_song(123)
    # show_default_song()                           # does not work, the first parameter is a required positional arg.

    use_flexible_arg_list('Songs', 'Because the Night', 'Till Victory', 'Dancing Barefoot')
    use_flexible_arg_list('Songs', 'Because the Night',)
    use_flexible_arg_list('Songs',)

    use_all_categories_of_args('Patti Smith\'s song', 'Easter', 'Greatest Hits',
                               author1='Bruce Springsteen', author2='Patti Smith')
    use_all_categories_of_args('Patti Smith\'s song', 'Easter',
                               author2='Patti Smith')
    use_all_categories_of_args('Patti Smith\'s song', 'Easter', song='Till Victory',
                               author2='Patti Smith')
    use_all_categories_of_args('Patti Smith\'s song', song='Till Victory')
    print()
                                                    # lambda examples
    authors = ['Bruce Springsteen', 'Patti Smith']
    sort_authors_reversed = lambda a: sorted(a, reverse=True)
    # sort_authors_reversed = lambda a: print(sorted(a, reverse=True))
    # sort_authors_reversed(authors)                # doesn't show anything, use print (either here or in lambda)
    print(sort_authors_reversed(authors))
    (lambda a: a.index('Patti Smith'))(authors)     # call a lambda without assignment (shows nothing)
    print((lambda a: a.index('Patti Smith'))(authors))


