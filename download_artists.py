
import json
import urllib

from bs4 import BeautifulSoup


#uo = urllib.urlopen("http://www.cmj.com/marathon/cmj-2012-artists/")
uo = open('CMJ2012Artists.html', 'r')

doc = uo.read()

soup = BeautifulSoup(doc)

h4s = soup.find_all('h4')

artists = [h4.string for h4 in h4s]

fp = open('artists.json', 'w')
data = json.dumps(artists)
fp.write(data)
fp.close()

print "Wrote %s artists to artists.json" % len(artists)
