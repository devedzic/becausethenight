'''Demonstrates tuples'''


def demonstrate_tuples():
    '''Creating and using tuples.'''

    bruce = ('Bruce', 'Springsteen')
    patti = ('Patti', 'Smith')
    print('2-tuples:', bruce, patti)
    print()

    bruce_family_name = ('Springsteen', )
    print('1-tuple:', bruce_family_name)
    mixed_type_4_tuple = (bruce_family_name, patti, "Because the Night", 1978)
    print('Mixed-type 4-tuple:', mixed_type_4_tuple)
    print()

def demonstrate_zip():
    '''Using the built-in zip() function with tuples and double-counter for-loop.'''

    first = ['Bruce', 'Patti', 'Because the Night']
    second = ['Springsteen', 'Smith', 1978]
    song = zip(first, second)
    print('song:', song)
    for a, b in song:
        print(a, b)

def demonstrate_packing():
    '''Packing and unpacking tuples.'''

    bruce = 'Bruce', 'Springsteen'
    print(bruce)
    print()

    bruce, springsteen = bruce
    print(bruce, springsteen)
