#!/usr/bin/env python
from scrapy.spider import BaseSpider
from Config import Config
from scrapy.selector import Selector
from cfp_item import CfpItem

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
    #The name used on the web_page: corresponded item field name
    headers_detail = {"when": "When", \
                      "where": "Where", \
                      "sub_dline": "Submission Deadline", \
                      "notif_due":"Notification Due", \
                      "final_due": "Final Version Due"}
    
    #Fetch the details 
    cfpitem["detail"] = sel.xpath('//div[@class="cfp"]').extract()[0].strip()
    #Fetch the link
    cfpitem["url"] = sel.xpath('//td[contains(text(),"Link")]/a/text()').extract()[0].strip()   
    #Fetch the event_name
    cfpitem["event_name"] = sel.xpath('//span[@typeof="v:Event"]/span[@property="v:description"]/text()').extract()[0].strip()
    #Fetch the when and where
    q_w = '//table[@class="gglu"]//tr[descendant::th[contains(text(),"{}")]]/td/text()'
    cfpitem["when"] = sel.xpath(q_w.format(headers_detail["when"])).extract()[0].strip()

    cfpitem["where"] = sel.xpath(q_w.format(headers_detail["where"])).extract()[0].strip()
 
    #Fetch the time related details
    q_d = '//table[@class="gglu"]//tr[descendant::th[contains(text(),"{}")]]/td//span[@property="v:startDate"]/text()'
    cfpitem["sub_dline"] = sel.xpath(q_d.format(headers_detail["sub_dline"])).extract()[0].strip()

    cfpitem["notif_due"] = sel.xpath(q_d.format(headers_detail["notif_due"])).extract()[0].strip()

    cfpitem["final_due"] = sel.xpath(q_d.format(headers_detail["final_due"])).extract()[0].strip()

    yield cfpitem 
