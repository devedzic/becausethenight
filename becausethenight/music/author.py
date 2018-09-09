"""Domain classes and functions related to the concept of author"""


from enum import Enum
from becausethenight.util import utility


class Genre(Enum):
    """The enum indicating the music genres that the music package accepts."""

    ROCK = 1
    BLUES = 2
    SOUL = 3
    INDIE = 4
    ACOUSTIC = 5


class Instrument(Enum):
    """The enum indicating the instruments that the music package accepts."""

    GUITAR = 1
    VOCALS = 2
    PIANO = 3
    BASS = 4
    DRUMS = 5
    MULTIPLE_INSTRUMENTS = 6


class PoetryType(Enum):
    """The enum indicating the poetry types that the music package accepts."""

    LYRIC = 1
    EPIC = 2
    DRAMATIC = 3


class Author:
    """The class describing the concept of author.
    It is assumed that an author is sufficiently described by his/her
    name, age, birth date, birth place, nationality, and whether he/she is still living or is deceased."""

    definition = "Creator or originator of an artwork."

    # def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True):
    #     self.name = name
    #     self.age = age
    #     self.birth_date = birth_date
    #     self.birth_place = birth_place
    #     self.nationality = nationality
    #     self.alive = alive

    def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True):
        self.__name = name
        self.age = age
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.nationality = nationality
        self.alive = alive

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name == 'unknown'

    def __str__(self):
        return (str(self.__name) + '\n' +
                '\t' + 'age: ' + str(self.age) + '\n' +
                '\t' + 'born: ' + utility.format_date(self.birth_date) + '\n' +
                '\t' + 'place of birth: ' + str(self.birth_place) + '\n' +
                '\t' + 'nationality: ' + str(self.nationality) + '\n' +
                '\t' + utility.alive_or_deceased(self.alive))

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.__name == other.name) and (self.birth_date == other.birth_date):
            return True
        else:
            return False

    @staticmethod
    def show_generic_definition():
        print(Author.definition)

    @classmethod
    def show_definition(cls):
        print(cls.definition)

    @classmethod
    def get_instance(cls, name):                            # alternative constructor
        if isinstance(name, str):
            return cls(name)
        else:
            return cls('unknown')


class Musician(Author):
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described as an Author, with addition of his/her
    music genre and instrument(s)."""

    definition = "A person who composes, conducts, or performs music."

    def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True,
                 genre=Genre.ROCK, instrument=Instrument.GUITAR):
        super().__init__(name, age, birth_date, birth_place, nationality, alive)
        self.genre = genre
        self.instrument = instrument

    def __str__(self):
        return (super().__str__() + '\n' +
                '\t' + 'genre: ' + self.genre.name.lower() + '\n' +
                '\t' + 'instrument(s): ' + self.instrument.name.lower())

    def __eq__(self, other):
        return super().__eq__(other)


class Poet(Author):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as an Author,
    with addition of the type of poetry they create."""

    definition = "A person who creates poetry."

    def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True,
                 poetry=PoetryType.LYRIC):
        super().__init__(name, age, birth_date, birth_place, nationality, alive)
        self.poetry = poetry

    def __str__(self):
        return (super().__str__() + '\n' +
                '\t' + 'poetry: ' + self.poetry.name.lower())

    def __eq__(self, other):
        return super().__eq__(other)


class SingerSongwriter(Musician, Poet):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as a Musician who is simultaneously a Poet."""

    definition = "A musician who writes, composes, and performs their own musical material (both lyrics and melodies)."

    def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True,
                 genre=Genre.ROCK, instrument=Instrument.GUITAR, poetry=PoetryType.LYRIC):
        Poet.__init__(self, name, poetry=poetry)
        Musician.__init__(self, name, age, birth_date, birth_place, nationality, alive, genre, instrument)

    def __str__(self):
        return (Musician.__str__(self) + '\n' +
                '\t' + 'poetry: ' + self.poetry.name.lower())

    def __eq__(self, other):
        return super().__eq__(other)


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
    print(bruceSpringsteen)                                                 # test __str__()
    print()

    bruce = Author('Bruce Springsteen',
                   birth_date=date(1949, 9, 23))
    if bruceSpringsteen == bruce:                                           # test __eq__()
        print(True)
    else:
        print(False)
    print()

    lennyKaye = Musician('Lenny Kaye', 70,                                  # test Musician
                         date(1948, 2, 21),
                         'New York City', 'US')
    print(lennyKaye)

    lenny = Musician('Lenny Kaye', 70,
                     date(1948, 2, 21))
    if lennyKaye == lenny:
        print('eq')
    else:
        print('not eq')
    print()

    edgarAllanPoe = Poet('Edgar Allan Poe', -1,                             # test Poet
                         date(1809, 1, 19),
                         'Boston', 'US', False)
    print(edgarAllanPoe)
    print()

    jonathanWilson = SingerSongwriter('Jonathan Wilson', 50,                # test SingerSongwriter (mult. inheritance)
                                      date(1968, 5, 29),
                                      'Boston', 'US', False)
    print(jonathanWilson)
    print()

    print(edgarAllanPoe.name)                                               # test name property (step through code)
    edgarAllanPoe.name = 'E. A. Poe'
    print(edgarAllanPoe.name)
    print()

    print('Just print static field:', edgarAllanPoe.definition)             # test static field/attribute
    edgarAllanPoe.definition = "An artist who creates poetry."
    print('Just print modified static field:', edgarAllanPoe.definition)    # show edgarAllanPoe fields in debugger
    print('Print modified static field from class:', Poet.definition)       # show Poet fields in debugger
    Poet.definition = "An artist who creates poetry."                       # modify static field from the class level
    print('Print modified static field again:', edgarAllanPoe.definition)
    print()

    print('Staticmethod called from a base class instance: ', end='')       # test staticmethod
    bruceSpringsteen.show_generic_definition()
    print('Staticmethod called from a subclass instance: ', end='')
    edgarAllanPoe.show_generic_definition()
    print('Staticmethod called from base class: ', end='')
    Author.show_generic_definition()
    print('Staticmethod called from subclass: ', end='')
    Poet.show_generic_definition()
    print()

    print('Classmethod called from a base class instance: ', end='')        # test classmethod
    bruceSpringsteen.show_definition()
    print('Classmethod called from a subclass instance: ', end='')
    edgarAllanPoe.show_definition()
    print('Classmethod called from base class: ', end='')
    Author.show_definition()
    print('Classmethod called from subclass: ', end='')
    Poet.show_definition()
    print()

    townesVanZandt = Musician.get_instance('Townes Van Zandt')              # test alternative constructor
    print(townesVanZandt)
    print()
