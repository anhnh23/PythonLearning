'''
Created on Dec 10, 2016

@author: ToOro
'''
"""Three common approaches to crawling a website:
+ Crawling a sitemap
+ Iterating the database IDs of each web page
+ Following web page links
"""
"""Technique
+ Proxy: use requests to apply proxy, reference at http://docs.python-requests.org
"""
url = "http://example.webscraping.com"
site_map = "http://example.webscraping.com/sitemap.xml"
index_view_pattern = '/(index|view)'
view_pattern = '/view'
user_agent = 'GoodCrawler' # this one is defined in robots.txt, we have to change to match
    # the one can be crawled
# just crawl a particular web page
import download_util
import Queue
import re
import itertools

def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp', proxy=None, num_retries=1):
    """Crawl from the given seed URL following links matched by link_regex
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = Queue.deque([seed_url])
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}
    # track how many URL's have been downloaded
    num_urls = 0
    rp = download_util.get_robots(seed_url)
    throttle = download_util.Throttle(delay)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent
        
    while crawl_queue:
        url = crawl_queue.pop()
        # check ulr passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):
            throttle.wait(url)
            html = download_util.download(url, headers, proxy=proxy, num_retries=num_retries)
            links = []
            
            depth = seen[url]
            if depth != max_depth:
                # can still crawl further
                if link_regex:
                    # filter for links matching our regular expression
                    links.extend(link for link in download_util.get_links(html) if re.match(link_regex, link))
                
                for link in links:
                    link = download_util.normalize(seed_url, link)
                    # check weather already crawled this link
                    if link not in seen:
                        seen[link] = depth + 1
                        # check link is within same domain
                        if download_util.same_domain(seed_url, link):
                            #sccess! add this new link to queue
                            crawl_queue.append(link)
            # check whether have reached downloaded maximum
            num_urls += 1
            if num_urls == max_urls:
                break
        else:
            print 'Blocked by robots.txt', url

# ignore slug and iterate database IDs
def crawl_all_countries(user_agent='wswp', headers=None, num_retries=1):
    #maximum number of consecutive download errors allowed
    max_errors = 5
    # current number of consecutive download errors
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/{}'.format(page)
        html = download_util.download(url, headers={}, proxy=None)
        if html is None:
            # received and error trying to download this web page
            num_errors += 1
            if num_errors == max_errors:
                # reached maximum number of
                # consecutive errors so exit
                break
        else:
            #success - scrape the result here
            num_errors = 0

if __name__ == '__main__':
    #link_crawler(url, index_view_pattern, delay=0, num_retries=1, user_agent='BadCrawler')
    #link_crawler(url, index_view_pattern, delay=0, num_retries=1, max_depth=2, user_agent='GoodCrawler')
    #crawl all country
    crawl_all_countries(user_agent='GoodCrawler')
