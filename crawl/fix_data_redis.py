import os
import sys
import django
import redis
import time

from crawl import settings
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hiring.settings'

django.setup()

from apps.position.models import PositionOri

redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

while True:
    if redis_cli.scard("zhi_lian_items:id"):
        time.sleep(300)

    queryset = PositionOri.objects.filter(position_description__isnull=True)

    for position in queryset:
        redis_cli.sadd("zhi_lian_items:id", position.id)
