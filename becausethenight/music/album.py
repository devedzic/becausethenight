"""Domain classes and functions related to the concept of album"""


from becausethenight.util import utility


class Album:
    """The class describing the concept of album.
    It is assumed that an album is sufficiently described by its
    title, performer, duration and release date."""

    definition = 'A collection of audio recordings issued as a single item on CD, record, audio tape or another medium.'

    def __init__(self, title='', performer=None, songs=[], duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.songs = songs
        self.duration = duration
        self.release_date = release_date

        self.__i = 0                                            # iterator index

    def __str__(self):
        return (self.title + '\n' +
                '\t' + 'performer(s): ' + utility.format_performer(self.performer) + '\n' +
                '\t' + 'songs:' + '\n' +
                format_songs(self.songs) + '\n' +
                '\t' + 'duration: ' + utility.format_duration(self.duration) + '\n' +
                '\t' + 'released: ' + utility.format_date(self.release_date))

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.title == other.title) and (self.performer == other.performer):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__i + 1) <= len(self.songs):
            self.__i += 1
            return self.songs[self.__i - 1]
        else:
            raise StopIteration


def format_songs(songs):
    """Formats the album's song list for __str__()."""

    if isinstance(songs, list) and songs != []:
        return '\t\t' + '\n\t\t'.join(song.title for song in songs)
    else:
        return '\t\t' + 'not specified'


def generate_songs(songs):
    i = 0
    while i < len(songs):
        yield songs[i]
        i += 1


if __name__ == "__main__":

    from becausethenight.music.song import Song
    from becausethenight.music.performer import Performer
    from becausethenight.music.author import Author
    from datetime import date

    pattiSmithGroup = Performer("Patti Smith Group", is_band=True)
    bruce = Author("Bruce Springsteen")
    patti = Author("Patti Smith")
    bruce_and_patti = Author("Bruce Springsteen, Patti Smith")

    till_victory = Song("Till Victory",
                        performer=pattiSmithGroup,
                        author=patti,
                        duration=370,
                        release_date=date(1978, 2, 12))
    space_monkey = Song("Space Monkey",
                        performer=pattiSmithGroup,
                        author=patti,
                        duration=233,
                        release_date=date(1978, 1, 23))
    because_the_night = Song("Because the Night",
                             performer=pattiSmithGroup,
                             author=bruce_and_patti,
                             duration=333,
                             release_date=date(1978, 3, 2))

    songs = [till_victory, space_monkey, because_the_night]

    print('\tsongs:')                                           # test formatting a song list
    print(format_songs([]))
    print('\tsongs:')
    print(format_songs(songs))
    print()

    # for song in songs:
    #     print(song)
    # print()

    easter = Album('Easter')                                    # test formatting an Album object
    print(easter)
    easter = Album('Easter',
                   pattiSmithGroup,
                   songs,
                   2800,
                   date(1978, 3, 2))
    print(easter)
    print()

    s = 'Rock'                                                  # demonstrate iterators
    print('s:', s)
    s_iterator = iter(s)
    print('s_iterator:', s_iterator)
    print('Iterating through s:')
    for char in s:
        print(next(s_iterator))
    print()

    songs_iterator = iter(songs)
    print('songs_iterator:', songs_iterator)
    print('Iterating through songs:')
    for song in songs:
        print(next(songs_iterator))
    print()

    print('Iterating through songs from album:')
    for song in easter:
        print(song)
    print()

    def simple_generator():                                     # demonstrate generators
        yield("Patti Smith")
        yield("Bruce Springsteen")
        yield("Southside Johnny")
        yield("...")

    g = simple_generator()
    print("Great musicians:")
    for m in simple_generator():
        print('\t', m)
    print()

    print("Songs on the 'Easter' album:")
    for song in generate_songs(easter.songs):
        print(song)