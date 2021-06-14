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
    # 数据挖掘
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98")

    # 大数据
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE")

    # 机器学习
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0")

    # 人工智能
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD")

    # 区块链
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E5%8C%BA%E5%9D%97%E9%93%BE")

    # 数据架构
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84")

    # 数据开发
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E6%95%B0%E6%8D%AE%E5%BC%80%E5%8F%91")

    # 算法工程师
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88")

    # 深度学习
    redis_cli.rpush("zhi_lian:start_urls",
                    f"https://sou.zhaopin.com/?jl={code}&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0")
