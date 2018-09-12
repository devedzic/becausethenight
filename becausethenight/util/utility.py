"""Utility functions of the package music"""


from becausethenight.music import song

from enum import Enum
from datetime import date
import pickle
import json


def format_duration(seconds):
    """Converts a duration from seconds to string of the form '<mm>:<ss>'."""

    if seconds > 0:
        return "%d:%02d" % divmod(seconds, 60)
    else:
        return str(0)


def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'."""

    if isinstance(a_date, date):
        return a_date.strftime("%b %d, %Y")
    else:
        return 'unknown'


def alive_or_deceased(alive):
    """Converts the status of being alive or deceased from boolean to string."""

    if isinstance(alive, bool):
        return 'alive' if alive else 'deceased'
    elif isinstance(alive, Lives):
        return 'alive' if alive == Lives.ALIVE else 'deceased'
    else:
        return 'Alive/Deceased: unknown'

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


class Lives(Enum):
    """The enum indicating the status of being alive or deceased."""

    ALIVE = 1
    DECEASED = 2


def format_performer(performer):
    """Converts performer object to its name field, for printing purposes."""

    from becausethenight.music.performer import Performer

    if isinstance(performer, Performer):
        return performer.name
    else:
        return 'unknown'


def format_performer_type(performer):
    """Converts the flag of performer type from boolean to string, if needed."""

    from becausethenight.music.performer import Performer

    if isinstance(performer, Performer):
        return performer.name + ' (band)' if performer.is_band else ' (musician)'
    else:
        return 'unknown if band or musician'

    # Alternatively:
    # if isinstance(performer, Performer):
    #     if performer.is_band:
    #         return performer.name + ' (band)'
    #     else:
    #         return performer.name + ' (musician)'
    # else:
    #     return 'unknown if band or musician'


def format_author(author):
    """Converts performer object to its name field, for printing purposes."""

    from becausethenight.music.author import Author

    if isinstance(author, Author):
        return author.name
    else:
        return 'unknown'


def date_py_to_json(a_date):
    """Converts datetime.date objects to JSON."""

    return a_date.isoformat() if isinstance(a_date, date) else 'null'


def date_json_to_py(iso_date):
    """Converts string formatted as 'YYYY-mm-dd' to datetime.date object."""

    args = [int(x) for x in iso_date.split(sep='-')]
    return date(args[0], args[1], args[2]) if len(args) == 3 else None


if __name__ == '__main__':

    print()                                                             # demonstrate pickle.dumps() and pickle.loads()
    because_the_night = song.Song('Because the Night')
    print(because_the_night)
    print()
    pickle_example = pickle.dumps(because_the_night)
    print('pickle.dumps():', pickle_example)
    print()
    pickle_example = pickle.dumps(because_the_night, protocol=pickle.HIGHEST_PROTOCOL)
    print('pickle.dumps() using HIGHEST_PROTOCOL:', pickle_example)
    print()
    back_to_python = pickle.loads(pickle_example)
    print(back_to_python)
    # print(back_to_python == because_the_night)                        # returns True
    print()

    json_example = json.dumps([1, None, True, [1, 2, 3],                # demonstrate json.dumps() and json.loads()
                               {'6': 7, '4': 5}],
                              sort_keys=True, indent=4)
    print(json_example)
    print()
    back_to_python = json.loads(json_example)
    print(back_to_python)
    print()

    # print(json.dumps(date(1978, 3, 2)))                               # No!
                                                                        # Object of type 'date' is not JSON serializable

    release_date = date_py_to_json(date(1978, 3, 2))                    # test date object conversions
    print('date_py_to_json():', release_date)
    print('date_py_to_json():', date_py_to_json(None))
    print('date_json_to_py():', date_json_to_py(release_date))
    print()


