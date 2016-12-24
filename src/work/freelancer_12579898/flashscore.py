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

#url = 'http://www.flashscore.com/soccer/belgium/proximus-league/results/'
url = 'http://www.kenya-business-directory.com/listo/'
table_id = 'fs-results'
table_class = 'fs-table tournament-page'

def scrape(html):
    tree = lxml.html.fromstring(html)
    lis = tree.cssselect('div#content > li')
    for li in lis:
        print(li.text_content())

if __name__ == '__main__':
    html = request.urlopen(url).read()
    scrape(html)