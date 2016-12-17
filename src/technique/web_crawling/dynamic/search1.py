# -*- coding: utf-8 -*-
'''
Created on Dec 14, 2016

@author: ToOro
'''
import json
import string
from technique.web_crawling.util.common import Downloader
from technique.web_crawling import mongo_cache

FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')

def main():
    template_url = 'http://example.webscraping.com/ajax/search.json?page={}&page_size=10&search_term={}'
    countries = set()
    download = Downloader(mongo_cache.MongoCache())
    
    for letter in string.lowercase:
        page = 0
        while True:
            html = download(template_url.format(page, letter))
            try:
                ajax = json.loads(html)
            except ValueError as e:
                print e
                ajax = None
            else:
                for record in ajax['records']:
                    countries.add(record['country'])
            page += 1
            if ajax is None or page >= ajax['num_pages']:
                break
    open('countries.txt', 'w').write('\n'.join(sorted(countries)))
    
if __name__ == '__main__':
    main()