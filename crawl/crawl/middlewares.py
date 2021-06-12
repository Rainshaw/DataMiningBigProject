import json
import os
import platform
import random
import time

from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumMiddleware(object):
    isLogin = False

    def __init__(self):
        if platform.system() == "Windows":
            self.browser1 = webdriver.Chrome(
                executable_path=f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\chromedriver.exe')
        elif platform.system() == "Darwin":
            options = webdriver.ChromeOptions()
            options.add_argument("--proxy-server=socks5://162.105.145.137:1080")
            self.browser1 = webdriver.Chrome(
                executable_path=f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/chromedriver',
                chrome_options=options)
        else:
            raise Exception("不支持的操作系统！")
        self.browser1.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
        })

        self.login()
        self.homePageHandle1 = self.browser1.current_window_handle

    def login(self, ignore_cookie_file=False):
        if not ignore_cookie_file and os.path.exists('zhi_lian.json'):
            self.browser1.get("https://www.zhaopin.com/")
            with open('zhi_lian.json', 'r', encoding='utf-8') as f:
                list_cookies = json.loads(f.read())
            for cookie in list_cookies:
                if cookie['domain'] != '.zhaopin.com':
                    continue
                self.browser1.add_cookie({
                    'domain': cookie['domain'],
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'path': '/',
                    'expires': None
                })
        else:
            self.browser1.get("https://passport.zhaopin.com/login")
            input('请手动登录，登录好了之后回车：')
            cookies = self.browser1.get_cookies()
            json_cookies = json.dumps(cookies)
            with open('zhi_lian.json', 'w') as f:
                f.write(json_cookies)

        self.isLogin = True
        time.sleep(10)

    def process_request(self, request, spider):
        self.browser1.get(request.url)
        time.sleep(random.randint(8, 15))
        page_text = self.browser1.page_source

        try:
            self.browser1.find_element_by_class_name('page-empty__tips-login')
            self.login(ignore_cookie_file=True)
            return self.process_request(request, spider)
        except Exception:
            pass
        return HtmlResponse(url=self.browser1.current_url, body=page_text, encoding='utf-8', request=request)
