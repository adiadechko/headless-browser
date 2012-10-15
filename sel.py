#!/usr/bin/env python
#coding: utf-8

"""和 PyQt4 写的抓取同一个网页的程序抓取到的数据进行对比
"""

from selenium import webdriver


class SelDang(object):

    def __init__(self, url):
        self.url = url
        self.ff = webdriver.Firefox()
        self.get_pagesource()

    def get_pagesource(self):
        self.ff.get(self.url)
        with open('dangbook.txt', 'ab+') as fp:
            fp.write(self.ff.page_source.encode('utf-8', 'ignore'))


if __name__ == '__main__':
    url = 'http://product.dangdang.com/product.aspx?product_id=22848151'
    seldang = SelDang(url)
