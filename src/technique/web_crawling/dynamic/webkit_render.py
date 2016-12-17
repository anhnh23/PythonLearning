'''
Created on Dec 14, 2016

@author: ToOro
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import lxml.html
from technique.web_crawling.util import common

def direct_download(url):
    download = common.Downloader()
    return download(url)

def webkit_download(url):
    app = QApplication([])
    webview = QWebView()
    webview.loadFinished.connect(app.quit)
    webview.load(QUrl(url))
    app.exec_() # delay here until download finished
    html = webview.page().mainFrame().toHtml()
    return str(html)

def parse(html):
    tree = lxml.html.fromstring(html)
    print(tree.cssselect('#result')[0].text_content())
    
def main():
    url = 'http://example.webscraping.com/dynamic'
    parse(direct_download(url))
    #parse(webkit_download(url))
    return

if __name__ == '__main__':
    main()

    
