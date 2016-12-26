'''
Created on Dec 22, 2016

@author: ToOro
'''
"""Requirement
Collecting data from links:
1. http://www.flashscore.com/soccer/belgium/proximus-league/results/
2. http://www.flashscore.com/soccer/belgium/proximus-league-2015-2016/results/
3. http://www.flashscore.com/soccer/belgium/proximus-league-2014-2015/results/
4. http://www.flashscore.com/soccer/belgium/proximus-league-2013-2014/results/
"""
import urllib.request as request
import lxml.html
from lxml.cssselect import CSSSelector 

url = 'http://www.flashscore.com/soccer/belgium/proximus-league/results/'
table_id = 'fs-results'
table_class = 'fs-table tournament-page'

def scrape(html):
    tree = lxml.html.fromstring(html)
    div = CSSSelector('div#fs-results')
    print(div.path)

if __name__ == '__main__':
    html = request.urlopen(url).read()
    scrape(html)