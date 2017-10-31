import urllib2
import os, sys
from bs4 import BeautifulSoup

gainers_url = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=L'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
gainers_page = opener.open('https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=L')
#gainers_page = urllib2.urlopen(gainers_url)
gainers_page_soup = BeautifulSoup(gainers_page,'html.parser')

#for name in gainers_page_soup.find_all(['table', 'tr', 'td', 'a'], attrs = {'id':'topGainers'}):
#	print name.text.encode('utf-8')

#for name in gainers_page_soup.find_all('a',):
 #   if name.text.encode('utf-8') == 'Nifty 50':
  #    print "TRUE"

for name in gainers_page_soup.find_all(['tr', 'td']):
	print name
