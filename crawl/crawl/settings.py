# Scrapy settings for crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hiring.settings'
import django

django.setup()

BOT_NAME = 'crawl'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'
LOG_LEVEL = 'INFO'

# Specify the host and port to use when connecting to Redis
REDIS_HOST = '162.105.145.22'
REDIS_PORT = 6379

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Enables stats shared based on Redis
STATS_CLASS = "scrapy_redis.stats.RedisStatsCollector"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'crawl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'cookie': 'x-zp-client-id=c37d0040-622f-46c0-9173-f7ac1290c163; sts_deviceid=179c805f3b47e0-06f76f29baac52-14463c1d-2073600-179c805f3b5d51; adfbid2=0; adfbid=0; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.google.com%2F; FSSBBIl1UgzbN7N443S=N72R3_5LBO..85j5Q6uMqmhUFqLhSkVWhonhN2K9eEnSFvuldileAMsST9Oy6KEb; _uab_collina=162324338583991768577437; locationInfo_search={%22code%22:%22530%22%2C%22name%22:%22%E5%8C%97%E4%BA%AC%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; ZPCITIESCLICKED=|530; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; selectCity_search=530; ssxmod_itna=iqfx9D0DuDyDBGDz=D2eEKGQfC2rCA4XKUDBw+Y4iNDnD8x7YDv+z5G+RiRYiC77Rv+dDRO5fsYir7GxTDE7f5WqH+DAoDhx7QDox0=DnxAQDj1oTeDxhPDrDDxGW8xiKODXxKtDADY5z0r0GDGPCDleD0rK7DCeDQx5DPxKDvxi8GrIoLxDazxHvm2adGhvOBhoODQ5Ch2PDUAuDTa+e7eh4TgG4tm2qPEGa==7xPaeqgSWTPxRDfOhebu5Pe1LDD==; ssxmod_itna2=iqfx9D0DuDyDBGDz=D2eEKGQfC2rCA4XKD8LjhxGN5KKGaKiKzTauCzx8h+BPY5aWAG7vhCCe87y07fQlk5x3XRir7tzd=Ab2b1qArOPpAGE+rPQ0Of=ipUs3QSu2k13Afuy3zIv5mtBlbr7W4DwhG3DjKD+hGDD; d4d6cd0b4a19fa72b8cc377185129bb7=2c17a009-284a-41be-b195-4dd9ed24ad07; sts_sid=179f4d093a3bf3-04fe3507e7f6bd-14463b1b-1764000-179f4d093a4cc1; ZP_OLD_FLAG=false; zp_passport_deepknow_sessionId=3cca43ffs18ed041ba8f58f59fe052060edd; at=79f2f981fd1441cdbce9ec3a71916e68; rt=97293b65dccf40d4986690a4077f0116; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221105878466%22%2C%22first_id%22%3A%22179c805f3c72bc-06198d22f0f0a3-14463c1d-2073600-179c805f3c8d9e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22179c805f3c72bc-06198d22f0f0a3-14463c1d-2073600-179c805f3c8d9e%22%7D; ZL_REPORT_GLOBAL={%22//www%22:{%22seid%22:%22bfce12759fb740abacf07b58a5c579d7%22%2C%22actionid%22:%2206a6d175-e1a0-4cc5-8f06-8d1e4a5a73d4-cityPage%22}%2C%22jobs%22:{%22funczoneShare%22:%22dtl_best_for_you%22%2C%22recommandActionidShare%22:%220fda2a63-cd18-48f0-8e9a-47cb9a4cca5b-job%22}%2C%22/resume/new%22:{%22actionid%22:%2203d6de7e-64bc-4237-b541-1461fc05ac83%22%2C%22funczone%22:%22addrsm_ok_rcm%22}}; sts_evtseq=7; acw_tc=2760827016233119235254824e5a32e010ef0618aaa276845459117bcab3a2; FSSBBIl1UgzbN7N443T=5j7d2Pi8xxVGsiBXzZ1ltGNhF.4iF27mu0YxZkUoaCtmmLMPlryF6cHhcQdWOzuVQF43VKB0TaykK1sdT0PtVwKaIavRzgnyGzQ1QQX.Gi.r2l3xWyV0Cca0lf9mP_oXbh0akwwbWYTCgrsVXGIH_9erCh8cbpdPjFXK.B.SbfDAtb8H0vKrtQ9ULNCpRKSGdma8LewyrBxhySKgUfaJou48idI9yny2boMp1LAM2OfOdWxAPQMC9J6XLsnZKgHwl7nqN31tXjZwQ3MOO1Ojeuc_J4nkzFgeZgUALyaABdQ6XTxfV0D_GBMWmfQodGmb9iaYJwBVJaIN1g14LtIM3xQSsoZ69RDZ2GOJTBe7SV8p.lg9cUpUcpcUyMcgV7Rewqe3; zpfe_probe_token=7226ca23s48e4f4bbb9d6794a1fb859c213d',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'crawl.middlewares.SeleniumMiddleware': 543,
}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'crawl.pipelines.CrawlPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
