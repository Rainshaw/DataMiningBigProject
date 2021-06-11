import redis
from crawl import settings

redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

city_code = {
    "其他": 512,
    '北京': 530,
    '天津': 531,
    '河北': 532,
    '山西': 533,
    '内蒙古': 534,
    '辽宁': 535,
    '吉林': 536,
    '黑龙江': 537,
    '上海': 538,
    '江苏': 539,
    '浙江': 540,
    '安徽': 541,
    '福建': 542,
    '江西': 543,
    '山东': 544,
    '河南': 545,
    '湖北': 546,
    '湖南': 547,
    '广东': 548,
    '广西': 549,
    '海南': 550,
    '重庆': 551,
    '四川': 552,
    '贵州': 553,
    '云南': 554,
    '西藏': 555,
    '陕西': 556,
    '甘肃': 557,
    '青海': 558,
    '宁夏': 559,
    '新疆': 560,
    '香港': 561,
    '澳门': 562,
    '台湾': 563
}

for code in city_code.values():
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98")
