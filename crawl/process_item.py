import redis
from crawl import settings

redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

city_code = {
    "北京": "530",
    "上海": "538",
    "广州": "763",
    "深圳": "765",
    "天津": "531",
    "武汉": "736",
    "西安": "854",
    "成都": "801",
    "大连": "600",
    "长春": "613",
    "沈阳": "599",
    "南京": "635",
    "济南": "702",
    "青岛": "703",
    "杭州": "653",
    "苏州": "639",
    "无锡": "636",
    "宁波": "654",
    "重庆": "551",
    "郑州": "719",
    "长沙": "749",
    "福州": "681",
    "厦门": "682",
    "哈尔滨": "622",
}

for code in city_code.values():
    redis_cli.lpush("zhi_lian:start_urls", f"https://sou.zhaopin.com/?jl={code}&kw=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98")


