"""Domain classes and functions related to the concept of album"""


from becausethenight.util import utility


class Album:
    """The class related to the concept of album.
    It is assumed that an album is sufficiently described by its
    title, performer, duration and release date."""

    definition = 'A collection of audio recordings issued as a single item on CD, record, audio tape or another medium.'

    def __init__(self, title='', performer=None, duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.duration = duration
        self.release_date = release_date

    def __str__(self):
        return (self.title + '\n' +
                '\t' + 'performer(s): ' + str(self.performer) + '\n' +
                '\t' + 'duration: ' + utility.format_duration(self.duration) + '\n' +
                '\t' + 'released: ' + utility.format_date(self.release_date))

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.title == other.title) and (self.performer == other.performer):
            return True
        else:
            return False


if __name__ == "__main__":

    from datetime import date


