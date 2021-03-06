"""Domain classes and functions related to the concept of author
"""


from datetime import date
from enum import Enum
import json

from becausethenight.util import utility


class Lives(Enum):
    """The enum indicating the status of being alive or deceased.
    """

    ALIVE = 1
    DECEASED = 2


class Genre(Enum):
    """The enum indicating the music genres that the music package accepts.
    """

    ROCK = 1
    BLUES = 2
    SOUL = 3
    INDIE = 4
    ACOUSTIC = 5


class Instrument(Enum):
    """The enum indicating the instruments that the music package accepts.
    """

    GUITAR = 1
    VOCALS = 2
    PIANO = 3
    BASS = 4
    DRUMS = 5
    MULTIPLE_INSTRUMENTS = 6


class PoetryType(Enum):
    """The enum indicating the poetry types that the music package accepts.
    """

    LYRIC = 1
    EPIC = 2
    DRAMATIC = 3


class Author:
    """The class describing the concept of author.
    It is assumed that an author is sufficiently described by his/her
    name, birth date, birth place, nationality, and whether he/she is still living or is deceased.
    """

    definition = "Creator or originator of an artwork."

    # def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True):
    #     self.name = name
    #     self.age = age
    #     self.birth_date = birth_date
    #     self.birth_place = birth_place
    #     self.nationality = nationality
    #     self.alive = alive

    # def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True):
    def __init__(self, name, birth_date=None, birth_place='unknown', nationality='unknown', alive=Lives.ALIVE):

        self.name = name
        self.birth_date = birth_date
        # self.__age = self.age
        self.birth_place = birth_place
        self.nationality = nationality
        self.alive = alive

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # self.__name = name
        # if not isinstance(name, str) or name == '':
        #     self.__name = 'unknown'

        # if isinstance(name, str) and name != '':
        #     self.__name = name
        # else:
        #     self.__name = 'unknown'
        self.__name = name if name and isinstance(name, str) else 'unknown'

    @property
    def age(self):
        return date.today().year - self.birth_date.year if isinstance(self.birth_date, date) else 'unknown'

    # def __str__(self):
    #     return (self.__name + '\n' +
    #             '\t' + 'born: ' + utility.format_date(self.birth_date) + '\n' +
    #             # '\t' + 'age: ' + str(self.__age) + '\n' +
    #             '\t' + 'age: ' + str(self.age) + '\n' +
    #             '\t' + 'place of birth: ' + str(self.birth_place) + '\n' +
    #             '\t' + 'nationality: ' + str(self.nationality) + '\n' +
    #             '\t' + Author.alive_or_deceased(self.alive))

    def __str__(self):
        return '{}\n\tborn: {}\n\tage: {}\n\tplace of birth: {}\n\tnationality: {}\n\t{}\n'.\
            format(self.name, str(self.birth_date) if isinstance(self.birth_date, date) else 'unknown',
                   str(self.age), self.birth_place, self.nationality, Author.alive_or_deceased(self.alive))

    # def __eq__(self, other):
    #     if self.__class__ != other.__class__:
    #         return False
    #     if (self.__name == other.name) and (self.birth_date == other.birth_date):
    #         return True
    #     else:
    #         return False

    def __eq__(self, other):
        return True if isinstance(other, Author) and other.name == self.name and other.birth_date == self.birth_date \
            else False

    @classmethod
    def show_definition(cls):
        print(cls.definition)

    @staticmethod
    def show_generic_definition():
        print(Author.definition)

    @classmethod
    def get_instance(cls, name):                            # alternative constructor
        # if isinstance(name, str):
        #     return cls(name)
        # else:
        #     return cls('unknown')
        return cls(name) if isinstance(name, str) else cls('unknown')

    @staticmethod
    def format_author(author):
        """Converts author object to its name field, for printing purposes.
        """

        # if isinstance(author, Author):
        #     return author.name
        # else:
        #     return 'unknown'
        return author.name if isinstance(author, Author) and isinstance(author.name, str) and author.name else 'unknown'

    @staticmethod
    def alive_or_deceased(alive):
        """Converts the status of being alive or deceased from boolean to string.
        """

        # if isinstance(alive, bool):
        #     return 'alive' if alive else 'deceased'
        # elif isinstance(alive, Lives):
        #     return 'alive' if alive == Lives.ALIVE else 'deceased'
        # else:
        #     return 'Alive/Deceased: unknown'
        return 'alive' if alive == Lives.ALIVE else 'deceased' if alive == Lives.DECEASED else 'alive/deceased: unknown'

    # def py_to_json(self):                                   # developed just for testing
    #     d = self.__dict__
    #     d['birth_date'] = utility.date_py_to_json(self.birth_date)
    #     # d['alive'] = True if self.alive == 'alive' else False if self.alive == 'deceased' else 'unknown'
    #     if self.alive == True or self.alive == Lives.ALIVE:
    #         d['alive'] = True
    #     elif self.alive == False or self.alive == Lives.DECEASED:
    #         d['alive'] = False
    #     else:
    #         d['alive'] = 'unknown'
    #     return d

    # def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True):
    #     self.__name = name
    #     self.age = age
    #     self.birth_date = birth_date
    #     self.birth_place = birth_place
    #     self.nationality = nationality
    #     self.alive = alive


# def format_author(author):
#     """Converts performer object to its name field, for printing purposes."""
#
#     if isinstance(author, Author):
#         return author.name
#     else:
#         return 'unknown'


# def alive_or_deceased(alive):
#     """Converts the status of being alive or deceased from boolean to string."""
#
#     if isinstance(alive, bool):
#         return 'alive' if alive else 'deceased'
#     elif isinstance(alive, Lives):
#         return 'alive' if alive == Lives.ALIVE else 'deceased'
#     else:
#         return 'Alive/Deceased: unknown'

    # Alternatively:
    # if isinstance(alive, bool):
    #     if alive:
    #         return 'alive'
    #     else:
    #         return 'deceased'
    # elif isinstance(alive, Lives):
    #     if alive == Lives.ALIVE:
    #         return 'alive'
    #     else:
    #         return 'deceased'
    # else:
    #     return 'Alive/Deceased: unknown'


class AuthorEncoder(json.JSONEncoder):
    """JSON encoder for Author objects.
    """

    def default(self, o):
        if isinstance(o, Author):
            d = o.__dict__.copy()
            d['birth_date'] = utility.date_py_to_json(o.birth_date)
            if o.alive or o.alive == Lives.ALIVE:
                d['alive'] = True
            elif not o.alive or o.alive == Lives.DECEASED:
                d['alive'] = False
            else:
                d['alive'] = 'unknown'
            return {'__Author__': d}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


def json_to_py(author_json):
    """JSON decoder for Author objects (object_hook parameter in json.loads()).
    """

    if '__Author__' in author_json:
        author = Author('')
        # performer = Performer('')
        # performer.__dict__.update(performer_json['__Performer__'])
        author.__dict__.update(author_json['__Author__'])
        author.birth_date = utility.date_json_to_py(author.birth_date)
        return author
    return author_json


class Musician(Author):
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described as an Author, with addition of his/her
    music genre and instrument(s).
    """

    definition = "A person who composes, conducts, or performs music."

    # def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', alive=True,
    #              genre=Genre.ROCK, instrument=Instrument.GUITAR):
    #     super().__init__(name, age, birth_date, birth_place, nationality, alive)

    def __init__(self, name, birth_date=None, birth_place='unknown', nationality='unknown', alive=Lives.ALIVE,
                 genre=Genre.ROCK, instrument=Instrument.GUITAR):
        super().__init__(name, birth_date, birth_place, nationality, alive)
        self.genre = genre
        self.instrument = instrument

    def __str__(self):
        return (super().__str__() + '\n' +
                '\t' + 'genre: ' + self.genre.name.lower() + '\n' +
                '\t' + 'instrument(s): ' + self.instrument.name.lower())

    def __eq__(self, other):
        return super().__eq__(other)

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre
        if not isinstance(genre, Genre):
            self.__genre = Genre.ROCK                           # default genre: ROCK

    @property
    def instrument(self):
        return self.__instrument

    @instrument.setter
    def instrument(self, instrument):
        self.__instrument = instrument
        if not isinstance(instrument, Instrument):
            self.__instrument = Instrument.GUITAR               # default instrument: GUITAR


class Poet(Author):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as an Author,
    with addition of the type of poetry they create.
    """

    definition = "A person who creates poetry."

    def __init__(self, name, birth_date=None, birth_place='unknown', nationality='unknown', alive=Lives.ALIVE,
                 poetry=PoetryType.LYRIC):
        super().__init__(name, birth_date, birth_place, nationality, alive)
        self.poetry = poetry

    def __str__(self):
        return (super().__str__() + '\n' +
                '\t' + 'poetry: ' + self.poetry.name.lower())

    def __eq__(self, other):
        return super().__eq__(other)

    @property
    def poetry(self):
        return self.__poetry

    @poetry.setter
    def poetry(self, poetry):
        self.__poetry = poetry
        if not isinstance(poetry, PoetryType):
            self.__poetry = PoetryType.LYRIC


class SingerSongwriter(Musician, Poet):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as a Musician who is simultaneously a Poet.
    """

    definition = "A musician who writes, composes, and performs their own musical material (both lyrics and melodies)."

    def __init__(self, name, birth_date=None, birth_place='unknown', nationality='unknown', alive=True,
                 genre=Genre.ROCK, instrument=Instrument.GUITAR, poetry=PoetryType.LYRIC):
        Poet.__init__(self, name, poetry=poetry)
        Musician.__init__(self, name, birth_date, birth_place, nationality, alive, genre, instrument)

    def __str__(self):
        return (Musician.__str__(self) + '\n' +
                '\t' + 'poetry: ' + self.poetry.name.lower())

    def __eq__(self, other):
        return super().__eq__(other)


if __name__ == "__main__":

    # from datetime import date

    # bruceSpringsteen = Author('Bruce Springsteen',
    #                           69,
    #                           date(1949, 9, 23),
    #                           'Freehold',
    #                           'US',
    #                           Lives.ALIVE)
    #
    # print(bruceSpringsteen)                                                 # test __str__()
    # print()

    # bruce = Author('Bruce Springsteen',
    #                birth_date=date(1949, 9, 23))
    # if bruceSpringsteen == bruce:                                           # test __eq__()
    #     print(True)
    # else:
    #     print(False)
    # print()

    # lennyKaye = Musician('Lenny Kaye',                                      # test Musician
    #                      date(1948, 2, 21),
    #                      'New York City', 'US')
    # print(lennyKaye)
    #
    # lenny = Musician('Lenny Kaye',
    #                  date(1948, 2, 21))
    # if lennyKaye == lenny:
    #     print('eq')
    # else:
    #     print('not eq')
    # print()

    # edgarAllanPoe = Poet('Edgar Allan Poe',                                 # test Poet
    #                      date(1809, 1, 19),
    #                      'Boston', 'US', Lives.DECEASED)
    # print(edgarAllanPoe)
    # print()

    # jonathanWilson = SingerSongwriter('Jonathan Wilson',                    # test SingerSongwriter (mult. inheritance)
    #                                   date(1968, 5, 29),
    #                                   'Boston', 'US', Lives.ALIVE)
    # print(jonathanWilson)
    #
    # jWilson = SingerSongwriter('Jonathan Wilson',                           # test super().__eq__()
    #                            date(1968, 5, 29),
    #                            'Boston', 'US', Lives.ALIVE)
    # if jonathanWilson == jWilson:
    #     print(True)
    # print()

    # print(edgarAllanPoe.name)                                               # test name property (step through code)
    # edgarAllanPoe.name = 'E. A. Poe'
    # print(edgarAllanPoe.name)
    # print()
    #
    # print('Just print static field:', edgarAllanPoe.definition)             # test static field/attribute
    # edgarAllanPoe.definition = "An artist who creates poetry."
    # print('Just print modified static field:', edgarAllanPoe.definition)    # show edgarAllanPoe fields in debugger
    # print('Print modified static field from class:', Poet.definition)       # show Poet fields in debugger
    # Poet.definition = "An artist who creates poetry."                       # modify static field from the class level
    # print('Print modified static field again:', edgarAllanPoe.definition)
    # print()
    #
    # print('Staticmethod called from a base class instance: ', end='')       # test staticmethod
    # bruceSpringsteen.show_generic_definition()
    # print('Staticmethod called from a subclass instance: ', end='')
    # edgarAllanPoe.show_generic_definition()
    # print('Staticmethod called from base class: ', end='')
    # Author.show_generic_definition()
    # print('Staticmethod called from subclass: ', end='')
    # Poet.show_generic_definition()
    # print()
    #
    # print('Classmethod called from a base class instance: ', end='')        # test classmethod
    # bruceSpringsteen.show_definition()
    # print('Classmethod called from a subclass instance: ', end='')
    # edgarAllanPoe.show_definition()
    # print('Classmethod called from base class: ', end='')
    # Author.show_definition()
    # print('Classmethod called from subclass: ', end='')
    # Poet.show_definition()
    # print()
    #
    # townesVanZandt = Musician.get_instance('Townes Van Zandt')              # test alternative constructor
    # print(townesVanZandt)
    # print()

    # bruceSpringsteen = Author('Bruce Springsteen',
    #                           69,
    #                           date(1949, 9, 23),
    #                           'Freehold',
    #                           'US',
    #                           Lives.ALIVE)

    # bruceSpringsteen = Author(name='Bruce Springsteen',
    #                           birth_date=date(1949, 9, 23),
    #                           birth_place='Freehold',
    #                           nationality='US',
    #                           alive=Lives.ALIVE)
    bruceSpringsteen = Author('',
                              date(1949, 9, 23),
                              'Freehold',
                              'US',
                              Lives.ALIVE)
    print(bruceSpringsteen)
    print(bruceSpringsteen.name)
    print(bruceSpringsteen.age)
    print()

    # bruceSpringsteen_json = json.dumps(bruceSpringsteen,                    # test JSON serialization/deserialization
    #                                    indent=4,
    #                                    cls=AuthorEncoder)
    # # bruceSpringsteen_json = bruceSpringsteen.py_to_json()
    # # print(type(bruceSpringsteen_json))
    # print(bruceSpringsteen_json)
    # print()
    #
    # bruce = json.loads(bruceSpringsteen_json, object_hook=json_to_py)
    # print(bruce)
    # print()
