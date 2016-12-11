# -*- coding: utf-8 -*-
'''
Created on Dec 10, 2016

@author: ToOro
'''
import urllib2
import urlparse
import robotparser
import re
from datetime import datetime, time

class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """
    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}
        
    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                # domain has been accessed recently
                # so need to sleep
                time.sleep(sleep_secs)
        # update the last accessed time
        self.domains[domain] = datetime.now()

def download(url, headers, proxy, num_retries=2, data=None):
    print 'Downloading:', url
    request = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if hasattr(e, 'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5xx http errors
                return download(url, headers, proxy, num_retries-1, data)
        else:
            code = None
    return html

def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser();
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp

def normalize(seed_url, link):
    """Normalize this URL by removing has and adding domain
    """
    link, _ = urlparse.urldefrag(link) #remove hash to avoid dupdicates
    return urlparse.urljoin(seed_url, link)

def same_domain(url1, url2):
    """Return True if both URL's belong to same domain
    """
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc
        
def get_links(html):
    """return a list of links from html
    """
    # a regular expression to extract all links from the web page
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

def crawl_sitemap(sitemap_url):
    sitemap = download(sitemap_url)
    links = re.findall('<loc>(.*?)</loc>', sitemap) # extract the sitemap links
    for link in links:
        html = download(link)
        # next is parse html content
    
