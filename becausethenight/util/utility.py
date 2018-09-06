"""Utility functions"""


from enum import Enum


def format_duration(seconds):
    """Converts a duration from seconds to string of the form '<mm>:<ss>'."""

    if seconds > 0:
        return "%d:%02d" % divmod(seconds, 60)
    else:
        return str(0)


def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'."""

    from datetime import date

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
    """The enum indicated the status of being alive or deceased."""

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


