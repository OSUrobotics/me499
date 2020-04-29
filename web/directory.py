#!/usr/bin/env python3


from bs4 import BeautifulSoup
from urllib.request import urlopen


if __name__ == '__main__':
    # This is a simple application to query phone numbers from the OSU directory database.

    # Build a url for the query.  We figured this out by interacting with the actual web site
    # while typing in some queries.  Notice that there's a {0} where we're going to insert the name that
    # people type in.
    url = 'http://directory.oregonstate.edu/?type=search&cn=&surname={0}&mail=&telephonenumber=&osualtphonenumber=&osuofficeaddress=&osudepartment=&affiliation=any&anyphone='

    # Loop forever
    while True:
        # Get a name
        surname = input('Surname? ')

        # If the name is 'quit', then we'll take that as a sign we're done.
        if surname == 'quit':
            break

        # Open the web page that queries this name.  If you look at the HTML source for the results, you
        # can see some patterns in the information that it returns.  We'll use this to pick out the
        # information that we need.
        with urlopen(url.format(surname)) as results:
            html = results.read().decode()
            soup = BeautifulSoup(html, 'html.parser')

            # Find all of the div tags with an attribute 'class' with a value 'record'.  These are all
            # records for a person.  We figured this out by looking at the HTML source.
            for person in soup.find_all('div', {'class': 'record'}):
                # Build a list of email addresses for this person (in case there are multiples).  This looks
                # for all the anchor tags ('a') under the current person, with an attribute of 'class' that
                # has a value of 'email'.  The string inside the tag is the phone number.  Again, we
                # figured this out by looking at the web page HTML.
                emails = [p.string for p in person.find_all('a', {'class': 'email'})]

                # Print out the information in a format that we like.  There's a lot going on in this print statement,
                # so we'll break it down for you.  The name we get from the web page is Surname, Firstnames.  We can
                # get to this through person.h3.string (the contents of the first h3 tag under person).  We're going
                # to use the string function split() to break this into a list on the comma, which means we have a list
                # like ['Surname', 'Firstnames'].  Then, we use the * operator to pass this to the format() function
                # as if it was two arguments.  Notice that, in the format string, we have {1} {0}, so that it prints
                # out the arguments out of order.  So, format runs as if it was called like this:
                #  format('Surname', 'Firstnames', emails)
                # The last argument takes the list of emails, and joins them into a single string with the join()
                # function.  The interesting bit here is if there is nothing in the string.  In this case, the empty
                # string ('') will be passed to format.  If this happens, we want to print 'None listed' instead.
                # We can use short-circuit evaluation to help here.  The argument is an or statement.  How this works
                # is that if the first term in the or (the result of the join) evaluates to True, the value of the
                # expression is the value returned by join().  If it is false, then the second term in the or is
                # evaluated, and the value of the overall expression is the value of the second term.  This works
                # because the empty string evaluates to False in logical expressions.  So, if the join is the empty
                # string, 'None listed' is passed to format, otherwise the result of the join is passed.
                # This seems complicated, but this use of or and short-ciruit evaluation is a common programming
                # idiom, and can lead to compact code for cases like this.
                print('{1} {0}: {2}'.format(*person.h3.string.split(', '), '; '.join(emails) or 'None listed'))
