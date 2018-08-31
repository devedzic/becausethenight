"""Domain classes and functions related to the concept of song"""


class Song:
    """The class related to the concept of song.
    It is assumed that a song is sufficiently described by its
    title, author, duration and release date."""

    definition = "A single (and often standalone) work of music, " \
                 "typically intended to be sung by the human voice..."

    def __init__(self, title='', performer=None, author=None, duration=0, releaseDate=None):
        self.title = title
        self.performer = performer
        self.author = author
        self.duration = duration
        self.releaseDate = releaseDate

    def __str__(self):
        return (self.title + '\n' +
                '\t' + 'performer(s): ' + str(self.performer) + '\n' +
                '\t' + 'author(s): ' + str(self.author) + '\n' +
                # '\t' + 'duration: ' + str(self.duration) + '\n' +
                # '\t' + 'duration: ' + "%d:%02d" % divmod(self.duration, 60) + '\n' +
                '\t' + 'duration: ' + format_duration(self.duration) + '\n' +
                '\t' + 'released: ' + str(self.releaseDate))

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.title == other.title) and (self.performer == other.performer):
            return True
        else:
            return False

    def play(self):
        print('Playing:', self.author + ' - ', self.title + '...')


def format_duration(seconds):
    """Converts song duration from seconds to string of the form <mm>:<ss>."""

    return "%d:%02d" % divmod(seconds, 60)


if __name__ == "__main__":

    print()
    print('Definition:', Song.definition)               # class variable (like static field in Java)
    print()

    because_the_night = Song('Because the Night')       # creating objects and comparing them
    becauseTheNight = Song('Because the Night')
    print(because_the_night)
    if because_the_night == becauseTheNight:            # True, since the contents of the two objects are the same
        print(True)
    else:
        print(False)
    if because_the_night == 'Because the Night':        # False, since 'Because the Night' is a string, not a Song
        print(True)
    else:
        print(False)
    print()

    becauseTheNight.album = "Easter"                    # adding a field to the object "on the fly"
    print(becauseTheNight.album + ':', becauseTheNight.title)
    if because_the_night == becauseTheNight:            # True; the class remains the same
        print(True)
    else:
        print(False)
    print()
