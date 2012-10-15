#!/usr/bin/env python
#coding: utf-8

"""测试使用 PyQt4 抓取网页信息
"""

import sys

from PyQt4.QtCore import QUrl, SIGNAL
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebPage, QWebView

class WebPage(QWebPage):
    
    def javaScriptConsoleMessage(self, message, lineNumber, sourceID):
        sys.stderr.write('Javascritp error at line number %d\n' % (lineNumber))
        sys.stderr.write('%s\n' % (message, ))
        sys.stderr.write('Source ID: %s\n' % (sourceID, ))


class Crawler(QApplication):
    
    def __init__(self, url):
        super(Crawler, self).__init__(sys.argv)
        self.url = url
        self.web_view = QWebView()
        self.web_page = WebPage()
        self.web_view.setPage(self.web_page)

        print 'Before connecting'
        self.connect(self.web_view, SIGNAL('loadFinished(bool)'), self.loadFinished)
        print 'After connecting'

        print 'Before loading'
        self.web_page.currentFrame().load(QUrl(self.url))
        print 'After loading'
        
    def loadFinished(self, ok):
        print 'In callback, before writing'
        with open('dang.txt', 'ab+') as fp:
            fp.write(self.web_page.currentFrame().toHtml().toUtf8())
        print 'In callback, after writing'


if __name__ == '__main__':
    # url = 'http://product.dangdang.com/product.aspx?product_id=22848151'
    url = 'http://www.360buy.com/product/707047.html'
    crawler = Crawler(url)
    sys.exit(crawler.exec_())
