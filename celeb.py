#import libraries

import urllib2
import os, sys
from bs4 import BeautifulSoup

celeb_page = 'http://www.imdb.com/search/name?birth_monthday=10-26&refine=birth_monthday&ref_=nv_cel_brn_1'
imdb_page = 'http://www.imdb.com'

imdb = urllib2.urlopen(imdb_page)
page = urllib2.urlopen(celeb_page)
soup = BeautifulSoup(page,'html.parser')
#c_name_box = soup.find_all('td', attrs = {'class':'name'})
for name in soup.find_all(['td', 'a'], attrs = {'class':'name'}):
#	c_name = c_name_box.text.strip(name)
#        c_name = name.text.strip()
	print name.text.encode('utf-8')

print "*******Experiment-print only names of celebs*******"

for ana in soup.findAll('a'):
  if ana.parent.name == 'td':
    print ana.text.encode('utf-8')


print celeb_page
