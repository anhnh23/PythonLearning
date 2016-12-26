'''
Created on Dec 23, 2016

@author: ToOro
'''
import urllib.request as request
import lxml.html

url = 'http://www.kenya-business-directory.com/listo/'
def scrape(html):
    tree = lxml.html.fromstring(html)
    lis = tree.cssselect('#content li')
    for li in lis:
        print(li.text_content())

if __name__ == '__main__':
    html = request.urlopen(url).read()
    scrape(html)
