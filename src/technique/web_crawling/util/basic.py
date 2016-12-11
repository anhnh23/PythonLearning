'''
Created on Dec 10, 2016

@author: ToOro
'''

"""Installing a module if not exist by command
pip install module/package_name
"""

# Identifying the technology used by a website
url = "http://example.webscraping.com"
import builtwith
print builtwith.parse(url)

# Finding the owner 
import whois
print whois.whois(url)

