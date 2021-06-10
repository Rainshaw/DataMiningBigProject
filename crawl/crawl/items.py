# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
from apps.position.models import Position


class PositionSpiderItem(DjangoItem):
    django_model = Position


# class CrawlItem(scrapy.Item):
#
#     position_name = scrapy.Field()
#     company_name = scrapy.Field()
#     company_class = scrapy.Field()
#     company_scale = scrapy.Field()
#     detail_url = scrapy.Field()
#
#     position_base = scrapy.Field()
#     position_experience = scrapy.Field()
#     position_degree = scrapy.Field()
#     position_vacancies = scrapy.Field()
#     position_min_salary = scrapy.Field()
#     position_max_salary = scrapy.Field()
#     position_update_time = scrapy.Field()
#     position_description = scrapy.Field()
#     position_welfare = scrapy.Field()
#     position_location = scrapy.Field()
