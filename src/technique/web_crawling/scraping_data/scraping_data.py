'''
Created on Dec 10, 2016
This one we need to install:
+ beautifulsoup4 - for parsing a web page and navigating content.
@author: ToOro
'''
import urllib2
from bs4 import BeautifulSoup
from technique.web_crawling.util import common
import re

def scrape(html):
    soup = BeautifulSoup(html)
    tr = soup.find(attrs={'id':'places_area__row'}) # locate the area row
    # 'class' is a special python attribute so instead 'class_' is used
    td = tr.find(attrs={'class':'w2p_fw'}) # locate the area tag
    area = td.text # extract the area contents from this tag
    return area

def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, 
                 user_agent='wswp', proxy=None, num_retries=1, scrape_callback=None):
    """Crawl from the given seed URL following links matched by link_regex
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = [seed_url]
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}
    # track how many URL's have been downloaded
    num_urls = 0
    rp = common.get_robots(seed_url)
    throttle = common.Throttle(delay)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent
    
    while crawl_queue:
        url = crawl_queue.pop()
        depth = seen[url]
        # check robots restriction
        if rp.can_fetch(user_agent, url):
            throttle.wait(url)
            html = common.download(url, headers, proxy=proxy, num_retries=num_retries)
            links = []
            if scrape_callback:
                links.extend(scrape(url, html) or [])
            
            if depth != max_depth:
                # can still crawl further
                if link_regex:
                    #filter for links matching our regular expression
                    links.extend(link for link in common.get_links(html) if re.match(link_regex, link))
                    
                for link in links:
                    link = common.normalize(seed_url, link)
                    # check whether already crawled this link
                    if link not in seen:
                        seen[link] = depth + 1
                        # check link is within same domain
                        if common.same_domain(seed_url, link):
                            # success! and this new link to queue
                            crawl_queue.append(link)
            # check whether have reached downloaded maximum
            num_urls += 1
            if num_urls == max_urls:
                break
        else:
            print 'Blocked by robots.txt:', url

if __name__ == '__main__':
    #html = urllib2.urlopen('http://example.webscraping.com/view/United-Kingdom-239').read()
    #print scrape(html)
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')
    