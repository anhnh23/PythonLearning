'''
Created on Dec 10, 2016

@author: ToOro
'''
import urllib.request as request
import urllib.parse as urlparse
import urllib.robotparser as robotparser
import re
from technique.web_crawling import Downloader
        
        
def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, 
                 headers=None, user_agent='wswp', proxies=None, num_retries=1,
                 scrape_callback=None, cache=None):
    """Crawl from the given seed URL following links matched by link_regex
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = [seed_url]
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}
    # track how many URL's have been downloaded
    num_urls = 0
    rp = get_robots(seed_url)
    '''
    throttle = Throttle(delay)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent
    '''
    D = Downloader(delay=delay, user_agent=user_agent, proxies=proxies,
                   num_retries=num_retries, cache=cache)
    while crawl_queue:
        url = crawl_queue.pop()
        depth = seen[url]
        # check robots restriction
        if rp.can_fetch(user_agent, url):
            #throttle.wait(url) commented 'cause using Downloader
            #html = download(url, headers, proxy=proxy, num_retries=num_retries)
            html = D(url)
            links = []
            if scrape_callback:
                #links.extend(scrape(url, html) or [])
                links.extend(scrape_callback(url, html) or [])
            
            if depth != max_depth:
                # can still crawl further
                if link_regex:
                    #filter for links matching our regular expression
                    links.extend(link for link in get_links(html) if re.match(link_regex,
                                                                              link))
                for link in links:
                    link = normalize(seed_url, link)
                    # check whether already crawled this link
                    if link not in seen:
                        seen[link] = depth + 1
                        # check link is within same domain
                        if same_domain(seed_url, link):
                            # success! and this new link to queue
                            crawl_queue.append(link)
            # check whether have reached downloaded maximum
            num_urls += 1
            if num_urls == max_urls:
                break
        else:
            print('Blocked by robots.txt:', url)
            
def download(url, headers, proxy, num_retries=2, data=None):
    print('Downloading:', url)
    request = request.Request(url, data, headers)
    opener = request.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(request.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except request.URLError as e:
        print('Download error:', e.reason)
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