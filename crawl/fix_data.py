import os
import random
import sys
import time
import redis
import django
import platform
from selenium import webdriver
from scrapy.http import HtmlResponse
from crawl import settings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hiring.settings'

django.setup()

from apps.position.models import PositionOri

options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=socks5://127.0.0.1:1080")
if platform.system() == "Darwin":
    browser1 = webdriver.Chrome(executable_path=f'{os.path.dirname(os.path.abspath(__file__))}/chromedriver',
                                chrome_options=options)
elif platform.system() == "Windows":
    browser1 = webdriver.Chrome(executable_path=f'{os.path.dirname(os.path.abspath(__file__))}\\chromedriver.exe',
                                chrome_options=options)
else:
    raise Exception("不支持的操作系统！")

redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

print(options.arguments)

while True:
    try:
        position = PositionOri.objects.get(id=redis_cli.spop("zhi_lian_items:id"))
    except:
        continue
    if position.position_description is not None:
        continue
    browser1.get(position.detail_url)
    time.sleep(random.randint(10, 15))
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
    except Exception as e:
        print(e)
        print(f"save false, id: {position.id}, url: {position.detail_url}")

browser1.quit()
