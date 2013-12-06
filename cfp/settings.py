# Scrapy settings for cfp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cfp'

SPIDER_MODULES = ['cfp.spiders']
NEWSPIDER_MODULE = 'cfp.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cfp (+http://www.yourdomain.com)'

TEM_PIPELINES = [
  'scrapy_mongodb.MongoDBPipeline',
]

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'cfps'
MONGODB_UNIQUE_KEY = 'event-name'
