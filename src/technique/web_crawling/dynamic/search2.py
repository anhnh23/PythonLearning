# -*- coding: utf-8 -*-
'''
Created on Dec 14, 2016

@author: ToOro
'''
import json
import csv
import technique.web_crawling.util.common as common

def main():
    writer = csv.writer(open('countries.csv', 'w'))
    D = common.Downloader()
    html = D('http://example.webscraping.com/ajax/search.json?page=0&page_size=1000&search_term=.')
    ajax = json.loads(html)
    print ajax
    for record in ajax['records']:
        writer.writerow([record['country']])

if __name__ == '__main__':
    main()