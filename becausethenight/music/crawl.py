"""Web crawling and scraping
"""

import requests
from bs4 import BeautifulSoup


def crawl(url, max_pages=1):
    """Web crawler that collects info about albums from the Web.
    Parameters: the url of the starting Web page and the max number of pages to crawl in case of multi-page lists.
    """

    page = 1
    # page_text = '***'
    soups = []

    while page <= max_pages:
        current_url = url + '?page=' + str(page)
        response = requests.get(current_url, allow_redirects=False)  # create Response object from GET request
        response_text = response.text  # get text from the Response object

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

        soup = BeautifulSoup(response_text, 'html.parser')  # create BeautifulSoup object from response text
        soups.append(soup)

        page += 1
    # return page_text
    return soups


if __name__ == "__main__":

    pass

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


