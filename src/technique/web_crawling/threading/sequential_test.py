# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2016

@author: ToOro
'''
from technique.web_crawling.util.common import link_crawler
from technique.web_crawling.mongo_cache import MongoCache
from alexa_cb import AlexaCallback

def main():
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    # cache.clear()
    link_crawler(seed_url=scrape_callback.seed_url, cache_callback=cache, scrape_callback=scrape_callback)
    
if __name__ == '__main__':
    main()