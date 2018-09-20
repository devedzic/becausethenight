"""Domain classes and functions related to the concept of album"""


from becausethenight.util import utility

import requests
from bs4 import BeautifulSoup


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


class AlbumError(Exception):
    """Base class for exceptions in this module."""

    pass


class SongNotIncludedError(AlbumError):
    """Exception raised when a song from an album is requested,
    but is not included in the list of songs from that album."""

    def __init__(self, song, album):
        self.song = song
        self.album = album
        self.message = "SongNotIncludedError: song \'{}\' not included on album \'{}\'".format(song.title, album.title)


def play_song(song, album):
    """Play the requested song from the album."""

    if song in album.songs:
        print(song)
    else:
        raise SongNotIncludedError(song, album)


def format_songs(songs):
    """Formats the album's song list for __str__()."""

    if isinstance(songs, list) and songs != []:
        return '\t\t' + '\n\t\t'.join(song.title for song in songs)
    else:
        return '\t\t' + 'not specified'


def generate_songs(songs):
    """A generator of Song objects, given the input list of songs."""

    i = 0
    while i < len(songs):
        yield songs[i]
        i += 1


def crawl(url, max_pages=1):
    """Web crawler that collects info about albums from the Web.
    Parameters: the url of the starting Web page and the max number of pages to crawl in case of multi-page lists."""

    page = 1
    # page_text = '***'
    soups = []

    while page <= max_pages:

        current_url = url + '?page=' + str(page)
        response = requests.get(current_url, allow_redirects=False)     # create Response object from GET request
        response_text = response.text                                   # get text from the Response object

        '''Encode response text as bytes object, using str.encode(encoding="utf-8", errors="strict").
        From str.encode() documentation: The errors argument specifies the response when the input string can’t be 
        converted according to the encoding’s rules. Legal values for this argument are 
        'strict' (raise a UnicodeDecodeError exception), 
        'replace' (use U+FFFD, REPLACEMENT CHARACTER), 
        'ignore' (just leave the character out of the Unicode result), 
        or 'backslashreplace' (inserts a \\xNN escape sequence).
        
        The following lines use str.encode() to prepare the text of the response for BeautifulSoup as a bytes object, 
        using encoding="utf-8" and errors="replace":
        
        response_text_bytes = response_text.encode('utf-8', 'replace')
        soup = BeautifulSoup(response_text_bytes, 'html.parser')
        
        The following line uses the response text directly as a string in the BeautifulSoup constructor 
        (encoding="utf-8" and errors="strict" is assumed, hence it can raise a UnicodeDecodeError exception):
        
        soup = BeautifulSoup(response_text, 'html.parser')
        
        The following line uses the response text directly as a string, as well as a default HTML parser
        (but issues a warning about it as well):
        
        soup = BeautifulSoup(response_text)
        '''

        soup = BeautifulSoup(response_text, 'html.parser')              # create BeautifulSoup object from response text
        soups.append(soup)

        page += 1
    # return page_text
    return soups


if __name__ == "__main__":

    # from becausethenight.music.song import Song
    # from becausethenight.music.performer import Performer
    # from becausethenight.music.author import Author
    # from datetime import date
    #
    # pattiSmithGroup = Performer("Patti Smith Group", is_band=True)
    # bruce = Author("Bruce Springsteen")
    # patti = Author("Patti Smith")
    # bruce_and_patti = Author("Bruce Springsteen, Patti Smith")
    #
    # till_victory = Song("Till Victory",
    #                     performer=pattiSmithGroup,
    #                     author=patti,
    #                     duration=370,
    #                     release_date=date(1978, 2, 12))
    # space_monkey = Song("Space Monkey",
    #                     performer=pattiSmithGroup,
    #                     author=patti,
    #                     duration=233,
    #                     release_date=date(1978, 1, 23))
    # because_the_night = Song("Because the Night",
    #                          performer=pattiSmithGroup,
    #                          author=bruce_and_patti,
    #                          duration=333,
    #                          release_date=date(1978, 3, 2))
    #
    # songs = [till_victory, space_monkey, because_the_night]
    #
    # print('\tsongs:')                                           # test formatting a song list
    # print(format_songs([]))
    # print('\tsongs:')
    # print(format_songs(songs))
    # print()
    #
    # # for song in songs:
    # #     print(song)
    # # print()
    #
    # easter = Album('Easter')                                    # test formatting an Album object
    # print(easter)
    # easter = Album('Easter',
    #                pattiSmithGroup,
    #                songs,
    #                2800,
    #                date(1978, 3, 2))
    # print(easter)
    # print()
    #
    # s = 'Rock'                                                  # demonstrate iterators
    # print('s:', s)
    # s_iterator = iter(s)
    # print('s_iterator:', s_iterator)
    # print('Iterating through s:')
    # for char in s:
    #     print(next(s_iterator))
    # print()
    #
    # songs_iterator = iter(songs)
    # print('songs_iterator:', songs_iterator)
    # print('Iterating through songs:')
    # for song in songs:
    #     print(next(songs_iterator))
    # print()
    #
    # print('Iterating through songs from album:')
    # for song in easter:
    #     print(song)
    # print()
    #
    # def simple_generator():                                     # demonstrate generators
    #     yield("Patti Smith")
    #     yield("Bruce Springsteen")
    #     yield("Southside Johnny")
    #     yield("...")
    #
    # g = simple_generator()
    # print("Great musicians:")
    # for m in simple_generator():
    #     print('\t', m)
    # print()
    #
    # print("Songs on the 'Easter' album:")
    # for song in generate_songs(easter.songs):
    #     print(song)
    # print()
    #
    # for i in range(5):                                          # demonstrate catching exceptions
    #     try:
    #         print(songs[i])
    #     # except IndexError:
    #     #     print("Exception: index out of bounds.")
    #     #     break
    #     # except IndexError as err:
    #     #     # print("Exception:", err.args, "(i = " + str(i) + ").")
    #     #     print("Exception:", err.args[0], "(i = " + str(i) + ").")
    #     #     break
    #     except IndexError as err:
    #         print("Exception:", err.args[0], "(i = " + str(i) + ").")
    #         break
    # print()
    #
    # for i in range(2):                                          # demonstrate catching multiple exceptions and finally
    #     try:
    #         print(songs[i])
    #         print(songs[i] / 4)
    #         print("Whatever...")
    #     except IndexError as err:
    #         print("Exception:", err.args[0], "(i = " + str(i) + ").")
    #         break
    #     except Exception as err:
    #         # print("Exception:", err.args[0])
    #         print(type(err).__name__ + ':', err.args[0])
    #         break
    #     finally:
    #         print("Stopped printing songs.")
    # print()
    #
    # for i in range(5):                                          # demonstrate catching "any" exception
    #     try:
    #         print(songs[i])
    #         print(songs[i] / 4)
    #     except:
    #         print("Caught an exception...")
    #         break
    # print()
    #
    # for i in range(5):                                          # demonstrate else clause (must be after all except's)
    #     try:
    #         print(songs[i])
    #     except IndexError as err:
    #         print("Exception:", err.args[0], "(i = " + str(i) + ").")
    #         break
    #     except Exception as err:
    #         # print("Exception:", err.args[0])
    #         print(type(err).__name__ + ':', err.args[0])
    #         break
    #     else:
    #         print("Executing the else clause...")
    # print()
    #
    # import sys
    # dancing_barefoot = Song('Dancing Barefoot')                 # demonstrate catching user-defined exception
    # # play_song(dancing_barefoot, easter)
    # try:
    #     play_song(dancing_barefoot, easter)
    # except SongNotIncludedError as err:
    #     print(err.message)
    #     # sys.stderr.write(err.message)                         # does not produce any output in PyCharm; a bug?
    # print()

    print()
    # BASE_URL = 'https://www.discogs.com'
    # start_url = 'https://www.discogs.com/artist/193816-Patti-Smith'
    # soup = crawl(start_url, 3)
    start_url = 'https://theculturetrip.com/north-america/usa/new-york/articles/five-essential-patti-smith-albums/'
    soups = crawl(start_url, 1)

    for soup in soups:
        # Just experimenting:
        # print(type(soup))
        # print(soup)
        # soup_file = utility.get_data_dir() / 'soup.html'
        # soup_file.write_text(str(soup), encoding='utf-8', errors='replace')

        # a_tags = \
        #     soup.find_all('a',
        #                   {'class':
        #                        "thumbnail_link thumbnail_size_small thumbnail_orientation_landscape thumbnail-lazyload "})
        # for tag in a_tags:
        #     tag.
        # print(a_tags[0])
        # print(a_tags[0].attrs)
        # a_tags_file = utility.get_data_dir() / 'a_tags.html'
        # a_tags_file.write_text(str(a_tags), encoding='utf-8', errors='replace')

        albums = []
        for link in soup.find_all('h2'):                        # get album titles
            # print(link.text)
            albums.append(link.text)

        album = iter(albums)
        for link in soup.find_all('img'):
            # print(link)
            src = link.get('src')
            # print(src)
            alt = link.get('alt')
            # print(alt)
            if src:
                if alt:                                         # if alt and alt != '', but '' also evaluates to False
                    print()
                    if '|' in alt:
                        print(album.__next__())
                    print(alt)
                    print(src)


