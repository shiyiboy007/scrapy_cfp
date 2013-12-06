#!/usr/bin/env python
from scrapy.spider import BaseSpider
import sys
sys.path.append("/root/lab2/cfp/cfp")
from Config import Config
from scrapy.selector import Selector

class CfpSpider(BaseSpider):
    config = Config()
    keyword = config.query.get("query","keyword")
    year = config.query.get("query","year")
    name = "CfpSpider"
    allowed_domains = ["http://www.wikicfp.com"]
    url_msg = "http://www.wikicfp.com/cfp/servlet/tool.search?q={}&year={}"
    start_urls = [url_msg.format(keyword, year)]
    
def parse(self, response):
    #All the content stocked are unicode strings
    sel = Selector(response)

    #Extract the hyperlinks
    urls = sel.xpath('//td[@align="left" and @rowspan="2"]/a[@href]/@href').extract()
    #Extract the event names
    events= sel.xpath('//td[@align="left" and @rowspan="2"]/a[@href]/text()').extract()

    for detail_link in urls:
        if detail_link:
            yield Request(url=allowed_domain+detail_link, callback=self.parse_detail) 

def parse_detail(self, response):
    cfpitem = CfpItem()
    sel = Selector(response)
    headers_detail = ["When", "Where", "Submission Deadline", "Notification Due", "Final Version Due"]
    
    #Extract the details 
    detail = sel.xpath('//div[@class="cfp"]').extract()[0]
    #Someplace for future analysis/transformation of html content
     
