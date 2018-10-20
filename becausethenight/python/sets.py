"""Demonstrates sets
"""


def demonstrate_sets():
    """Creating and using sets.
    """

    bruce = {'Bruce', 'Springsteen', 'Bruce'}
    print('No duplicates:', bruce)
    print()

    bruce = set('Bruce')
    springsteen = set('Springsteen')
    print('bruce:', bruce)
    print('springsteen', springsteen)
    print('bruce & springsteen:', bruce & springsteen)
    print('bruce | springsteen:', bruce | springsteen)
    print('bruce ^ springsteen:', bruce ^ springsteen)
    print('bruce - springsteen:', bruce - springsteen)
