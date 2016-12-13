# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2016

@author: ToOro
'''
import sys
from threaded_crawler import threaded_crawler
from technique.web_crawling.mongo_cache import MongoCache
from alexa_cb import AlexaCallback

def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    # cache.clear()
    threaded_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache,
                     max_threads=max_threads, timeout=10)
    
if __name__ == '__main__':
    max_threads = int(5)
    main(max_threads)