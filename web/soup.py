#!/usr/bin/env python3

# Beautiful Soup is a module that will let you parse data from HTML.  You can find out more about it here:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

# Request will allow you to grab web pages
from urllib.request import urlopen


if __name__ == '__main__':
    url = 'http://directory.oregonstate.edu'

    with urlopen(url) as page:
        html = page.read().decode()

        # Make an instance of Beautiful Soup to let us parse the information from the web page.
        soup = BeautifulSoup(html, 'html.parser')

        # Find all of the external links on this web page.  These will have the format
        #  <a href="some web page url">
        # So, we're going to look through all anchor tags (the "a"), for href attributes (which
        # will contain that urls)
        print('External links:')
        for anchor in soup.find_all('a'):
            print(' ', anchor.get('href'))

        # We can do better if we look at the contents of these links.  Actual external links start
        # with http: or https:, which define the protocol the browser should use to grab the data
        # (HyperText Transfer Protocol or the Secure version, in this case)
        print('Actual external links:')
        for anchor in soup.find_all('a'):
            if anchor.get('href')[:4] == 'http':
                print(' ', anchor.get('href'))
