import scrapy
import redis
from scrapy_redis.spiders import RedisSpider

from ..items import PositionSpiderItem
from .. import settings


class ZLSpider(RedisSpider):
    name = "zhi_lian"

    def __init__(self, **kwargs):
        self.redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
        super().__init__(**kwargs)

    def parse(self, response, **kwargs):
        positions = response.css('div.joblist-box__item')
        if not len(positions):
            return
        next_url = []
        flag = False
        for s in response.url.split('&'):
            if s.startswith('p='):
                flag = True
                s = s.split('=')
                s[1] = str(int(s[1]) + 1)
                s = '='.join(s)
            next_url.append(s)
        if not flag:
            next_url.append('p=2')
        next_url = '&'.join(next_url)
        print("++++++++++++++++++++++++++++")
        print(next_url)
        self.redis_cli.lpush("zhi_lian:start_urls", next_url)
        print("++++++++++++++++++++++++++++")
        for position in positions:
            url = position.css('a::attr(href)').get()
            item = PositionSpiderItem()
            item['position_name'] = position.css('span.iteminfo__line1__jobname__name::attr(title)').get()
            item['company_name'] = position.css('span.iteminfo__line1__compname__name::text').get()
            comdesc = position.css('span.iteminfo__line2__compdesc__item::text').getall()
            item['company_class'] = comdesc[0].strip()
            item["company_scale"] = comdesc[1].strip()
            item["detail_url"] = url
            jobdesc = position.css('ul.iteminfo__line2__jobdesc__demand li::text').getall()
            item["position_base"] = jobdesc[0].strip().split('-')[0]
            item["position_experience"] = jobdesc[1].strip()
            item["position_degree"] = jobdesc[2].strip()
            print(item.__dict__)
            yield scrapy.Request(url=url, meta={"meta_item": item}, callback=self.page_parse)

    def page_parse(self, response):
        item = response.meta['meta_item']
        try:
            vacancies = response.css('ul.summary-plane__info li::text').getall()
            if len(vacancies):
                vacancies = vacancies[-1]
            item['position_vacancies'] = int(vacancies.replace(u'人', '').replace(' ', '').replace(u'招', ''))

            salary = response.css('span.summary-plane__salary::text').get()
            if "面议" in salary:
                min_salary = max_salary = "面议"
            else:
                if '·' in salary:
                    salary = salary.split('·')[0]
                min_salary, max_salary = salary.split('-')
                if '万' in min_salary:
                    min_salary = float(min_salary[:-1]) * 10000
                elif '千' in min_salary:
                    min_salary = float(min_salary[:-1]) * 1000
                if '万' in max_salary:
                    max_salary = float(max_salary[:-1]) * 10000
                elif '千' in max_salary:
                    max_salary = float(max_salary[:-1]) * 1000
            item['position_min_salary'] = min_salary
            item['position_max_salary'] = max_salary

            item['position_update_time'] = response.css('span.summary-plane__time::text').get(). \
                replace(' ', '').replace(u'更新于', '')

            item['position_skill'] = ','.join(response.css('span.describtion__skills-item::text').getall())

            item['position_description'] = response.css('div.describtion__detail-content').get()

            item['position_welfare'] = ','.join(response.css('span.highlights__content-item::text').getall())

            item['position_location'] = response.css('span.job-address__content-text::text').get()
            print(item.__dict__)
        except Exception:
            pass
        finally:
            yield item
