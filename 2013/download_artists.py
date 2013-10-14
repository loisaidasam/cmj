
import json
import urllib

from bs4 import BeautifulSoup

URL_ARTISTS = 'http://www.cmj.com/marathon/cmj-2013-artists/'


def get_webpage_data():
    """Attempts to cache artist webpage in local file if it doesn't have it"""
    try:
        print "Attempting to grab local artists cached webpage..."
        with open('artists.html', 'r') as fp:
            print "Cool, got it!"
            return fp.read()
    except IOError:
        print "Didn't get it, downloading from %s ..." % URL_ARTISTS
        uo = urllib.urlopen(URL_ARTISTS)
        doc = uo.read()
        print "OK, caching locally..."
        with open('artists.html', 'w') as fp:
            fp.write(doc)
        print "OK"
        return doc

def main():
    doc = get_webpage_data()
    soup = BeautifulSoup(doc)

    artists = []

    artist_elements = soup.find_all('p')
    for artist_element in artist_elements:
        if '*' not in artist_element.text:
            continue
        artists += [artist.strip() for artist in artist_element.text.split('*')]

    fp = open('artists.json', 'w')
    data = json.dumps(artists)
    fp.write(data)
    fp.close()

    print "Wrote %s artists to artists.json" % len(artists)


if __name__ == '__main__':
    main()
