#!/usr/bin/env python3


# The request library lets you grab data from the web
import urllib.request as req

# JSON is a data format that is popular for web-delivered data, and the json module lets you unpack it easily
import json


if __name__ == '__main__':
    # This url delivers census data for Los Angeles.  Open it in your browser and take a look at the raw data
    url = 'https://data.lacity.org/api/views/nxs9-385f/rows.json'

    # You can open a web page just like you open a file, using urlopen().  Putting this in a with block
    # means it gets tidied up automatically when you're done with it.
    with req.urlopen(url) as source:
        # Get the data from the web site.  read() grabs the page and decode() take any strange characters and
        # reformats them so that Python will deal better with them.  loads() takes the result of this, and
        # parses out the data into a set of nested dictionaries.
        data = json.loads(source.read().decode())

        # Print out the names of the columns in the data.  Python doesn't really know what's there, so it's
        # up to you to interpret what's in the data, and what it means.  This will most likely be documented
        # on the data source web site.  Remember that JSON is delivered to you as a series of nested
        # dictionaries.  This is a very flexible data structure.
        print('Available data:')
        for i, column in enumerate(data['meta']['view']['columns']):
            print('  {0}: {1}'.format(i, column['name']))

        # Let's look at the zip code data.  The element called 'data' is a list of data elements.  Many of
        # these are strings, since JSON doesn't have any idea of what they actually are, and it's your
        # job to write code to cast them into something appropriate.  In this case, we're going to look at
        # columns 8 (Zip Code) and 9 (Population), and we're goingt o build a dictionary with this information
        # in it.  This duplicates the information that's already there, but it also reformats it into a form
        # where it's going to be easier for us to use.  We're going to keep the zip code as a string, but
        # we're going to cast the population to an integer.
        people = {}
        for datum in data['data']:
            people[datum[8]] = int(datum[9])

        # Now, we can use these data to answer some questions
        print('There were {0:,} people in LA in 2010.'.format(sum(n for n in people.values())))

        # How many zip codes have no people in them?
        empty = [zip for zip, n in people.items() if n == 0]
        print('{0} zip codes are empty ({1})'.format(len(empty), '; '.join(sorted(empty))))



