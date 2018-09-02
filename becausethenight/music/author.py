"""Domain classes and functions related to the concept of author"""


from becausethenight.util import utility


class Author:
    """The class related to the concept of author.
    It is assumed that an author is sufficiently described by his/her
    name, age, birth date, birth place, nationality, and whether he/she is still living or is deceased."""

    definition = "Creator or originator of an artwork."

    def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.nationality = nationality
        self.alive = alive

    def __str__(self):
        return (str(self.name) + '\n' +
                '\t' + 'age: ' + str(self.age) + '\n' +
                '\t' + 'born: ' + utility.format_date(self.birth_date) + '\n' +
                '\t' + 'place of birth: ' + str(self.birth_place) + '\n' +
                '\t' + 'nationality: ' + str(self.nationality) + '\n' +
                '\t' + utility.alive_or_deceased(self.alive))

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.name == other.name) and (self.birth_date == other.birth_date):
            return True
        else:
            return False


# The following functions have been moved to the utils.utility module:

# def alive_or_deceased(alive):
#     """Converts the status of being alive or deceased from boolean to string."""
#
#     if isinstance(alive, bool):
#         if alive:
#             return 'Alive'
#         else:
#             return 'Deceased'
#     elif isinstance(alive, Lives):
#         if alive == Lives.ALIVE:
#             return 'Alive'
#         else:
#             return 'Deceased'
#     else:
#         return 'Alive/Deceased: unknown'


if __name__ == "__main__":

    from datetime import date

    bruceSpringsteen = Author('Bruce Springsteen',
                              69,
                              date(1949, 9, 23),
                              'Freehold',
                              'US',
                              utility.Lives.ALIVE)
    print(bruceSpringsteen)                             # test __str__()
    print()

    bruce = Author('Bruce Springsteen',
                   birth_date=date(1949, 9, 23))
    if bruceSpringsteen == bruce:                       # test __eq__()
        print(True)
    else:
        print(False)
    print()



