import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html'%page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

import string, urllib2
def simple_url_page(url , begin_page , end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i, 5) + 'html'
        print "loading the "+ str(i) +" page, save as "+ sName+ " ....."
        f = open(sName, 'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

