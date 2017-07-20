'''
Created on Jul 17, 2017

@author: ToOro
'''
import urllib.request
import re
import itertools
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as error:
        print('Download error:', error.reason)
        html = None
        # retry
        if num_retries > 0:
            # get code to parse
            if hasattr(error, 'code') and 500 <= error.code < 600:
                #recursively retry 5xx http errors
                return download(url, num_retries - 1)
    return html

def crawl_sitemap(url):
    # downloading sitemap
    sitemap = download(url)
    # extracting the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # downloading each link
    for link in links:
        html = download(link)
        #scrape html here
        
'''Crawl site based on max errors'''
def crawl_site(url, max_errors=5):
    num_errors = 0
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = download(pg_url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                # reach max number of errors, so exit
                break
        else:
            num_errors = 0
            # sucess - can scrape the result

#crawl_sitemap('http://example.webscraping.com/sitemap.xml')
crawl_site('http://example.webscraping.com/places/default/index/')