# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2016

@author: ToOro
'''
import sys
from mongo_cache import MongoCache
from technique.web_crawling.threading.alexa_cb import AlexaCallback
from technique.web_crawling.threading.process_crawler import process_crawler

def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    cache.clear()
    process_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache,
                    max_threads=max_threads, timeout=10)
    
if __name__ == '__main__':
    max_threads = int(sys.argv[1])
    main(max_threads)