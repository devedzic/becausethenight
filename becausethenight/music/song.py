"""Domain classes and functions related to the concept of song"""


from becausethenight.util import utility
from becausethenight.music import performer, author


class Song:
    """The class describing the concept of song.
    It is assumed that a song is sufficiently described by its
    title, performer, author, duration and release date."""

    definition = "A single (and often standalone) work of music, " \
                 "typically intended to be sung by the human voice..."

    def __init__(self, title='', performer=None, author=None, duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.author = author
        self.duration = duration
        self.release_date = release_date

    def __str__(self):
        return (self.title + '\n' +
                '\t' + 'performer(s): ' + performer.format_performer_type(self.performer) + '\n' +
                '\t' + 'author(s): ' + author.format_author(self.author) + '\n' +
                # '\t' + 'duration: ' + str(self.duration) + '\n' +
                # '\t' + 'duration: ' + "%d:%02d" % divmod(self.duration, 60) + '\n' +
                '\t' + 'duration: ' + utility.format_duration(self.duration) + '\n' +
                # '\t' + 'released: ' + str(self.releaseDate))
                '\t' + 'released: ' + utility.format_date(self.release_date))

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.title == other.title) and (self.performer == other.performer):
            return True
        else:
            return False

    def play(self):
        # print('Playing:', self.author + ' - ', self.title + '...')
        # print('Playing:', str(self.author) + ' -', self.title + '...')
        print('Playing:', author.format_author(self.author) + ' -', self.title + '...')

# The following functions have been moved to the utils.utility module:

# def format_duration(seconds):
#     """Converts a duration from seconds to string of the form '<mm>:<ss>'."""
#
#     if seconds > 0:
#         return "%d:%02d" % divmod(seconds, 60)
#     else:
#         return str(0)
#
#
# def format_date(a_date):
#     """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'."""
#
#     from datetime import date
#
#     if isinstance(a_date, date):
#         return a_date.strftime("%b %m, %Y")
#     else:
#         return 'unknown'


if __name__ == "__main__":

    print()
    print('Definition:', Song.definition)               # class variable (like static field in Java)
    print()

    because_the_night = Song('Because the Night')       # creating objects and comparing them
    becauseTheNight = Song('Because the Night',
                           duration=333)
    print(because_the_night)
    print(becauseTheNight)
    print()

    if because_the_night == becauseTheNight:            # True, since the contents (according to __eq__()) are the same
        print(True)
    else:
        print(False)
    if because_the_night == 'Because the Night':        # False, since 'Because the Night' is a string, not a Song
        print(True)
    else:
        print(False)
    print()

    becauseTheNight.album = "Easter"                    # adding a field to the object "on the fly"
    print(becauseTheNight.album + ':',
          becauseTheNight.title)
    if because_the_night == becauseTheNight:            # True; the class remains the same
        print(True)
    else:
        print(False)
    print()

    because_the_night.play()                            # run an instance method
    print()

    from becausethenight.music.performer import Performer
    from becausethenight.music.author import Author
    from datetime import date

    pattiSmithGroup = Performer("Patti Smith Group", is_band=True)
    bruce_and_patti = Author("Bruce Springsteen, Patti Smith")
    because_the_night = Song("Because the Night",
                             performer=pattiSmithGroup,
                             author=bruce_and_patti,
                             duration=333,
                             release_date=date(1978, 3, 2))
    print(because_the_night)
    print()

    # print('Writing to a text file...')                  # demonstrate writing to a text file
    # with open('because_the_night.txt', 'w') as outfile:
    #     outfile.write(str(because_the_night))
    # print()
    #
    # print('Reading from a text file...')                # demonstrate reading from a text file
    # with open('because_the_night.txt', 'r') as infile:
    #     s = infile.read()
    # print(s)
    # print()

    print('Writing to a binary file...')                # demonstrate writing to a binary file
    with open('because_the_night.txt', 'wb') as outfile:
        outfile.write(str.encode(str(because_the_night)))
    print()

    print('Reading from a text file...')                # demonstrate reading from a binary file
    with open('because_the_night.txt', 'rb') as infile:
        s = infile.read()
    print(s)
    print()

