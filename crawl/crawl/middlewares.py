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
            self.browser2 = webdriver.Chrome(
                executable_path=f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\chromedriver.exe')
        elif platform.system() == "Darwin":
            options = webdriver.ChromeOptions()
            options.add_argument("--proxy-server=socks5://162.105.145.137:1080")
            self.browser1 = webdriver.Chrome(
                executable_path=f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/chromedriver',
                chrome_options=options)
            self.browser2 = webdriver.Chrome(
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
        self.browser2.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                            Object.defineProperty(navigator, 'webdriver', {
                              get: () => undefined
                            })
                          """
        })
        self.login()
        self.homePageHandle1 = self.browser1.current_window_handle

    def login(self):
        self.browser1.get("https://passport.zhaopin.com/login")
        input('请手动登录，登录好了之后回车：')
        self.isLogin = True

    def process_request(self, request, spider):
        if request.meta.get('meta_item') is not None:
            self.browser2.get(request.url.split('?')[0])
            time.sleep(random.randint(8, 15))
            page_text = self.browser2.page_source
            return HtmlResponse(url=self.browser2.current_url, body=page_text, encoding='utf-8', request=request)
        else:
            self.browser1.get(request.url)
            time.sleep(random.randint(8, 15))
            page_text = self.browser1.page_source
            return HtmlResponse(url=self.browser1.current_url, body=page_text, encoding='utf-8', request=request)
