# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CfpItem(Item):
    # define the fields for your item here like:
    url = Field()
    event_name = Field()
    when = Field()
    where = Field()
    detail = Field()
    sub_dline = Field()
    notif_due = Field()
    final_due = Field()

