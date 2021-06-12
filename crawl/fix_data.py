import os
import random
import sys
import time
import redis
import django
from selenium import webdriver
from scrapy.http import HtmlResponse
from crawl import settings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hiring.settings'

django.setup()

from apps.position.models import PositionOri

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=socks5://162.105.145.137:1080")
browser1 = webdriver.Chrome(executable_path=f'{os.path.dirname(os.path.abspath(__file__))}/chromedriver',
                            chrome_options=options)

redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

while True:
    position = PositionOri.objects.get(id=redis_cli.spop("zhi_lian_items:id"))
    if position.position_description is not None:
        continue
    browser1.get(position.detail_url)
    time.sleep(random.randint(8, 12))
    response = HtmlResponse(url=browser1.current_url, body=browser1.page_source, encoding='utf-8')
    try:
        position.position_vacancies = response.css('ul.summary-plane__info li::text').getall()[-1]

        position.position_salary = response.css('span.summary-plane__salary::text').get()

        position.position_update_time = response.css('span.summary-plane__time::text').get()

        position.position_skill = ','.join(response.css('span.describtion__skills-item::text').getall())

        position.position_description = response.css('div.describtion__detail-content').get()

        position.position_welfare = ','.join(response.css('span.highlights__content-item::text').getall())

        position.position_location = response.css('span.job-address__content-text::text').get()

        position.save()
        print(f"save true, id: {position.id}")
    except:
        print(f"save false, id: {position.id}, url: {position.detail_url}")


browser1.quit()
