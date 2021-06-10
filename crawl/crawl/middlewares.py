import os
import platform
import time

from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumMiddleware(object):
    isLogin = False

    def __init__(self):
        if platform.system() == "Windows":
            self.browser = webdriver.Chrome(
                executable_path=f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\chromedriver.exe')
        elif platform.system() == "Darwin":
            self.browser = webdriver.Chrome(
                executable_path=f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/chromedriver')
        else:
            raise Exception("不支持的操作系统！")
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
        })
        self.loadTime = 10
        self.login()

        self.homePageHandle = self.browser.current_window_handle

    def login(self):
        self.browser.get("https://passport.zhaopin.com/login")
        input('请手动登录，登录好了之后回车：')
        self.isLogin = True

    def process_request(self, request, spider):
        if request.meta.get('meta_item') is not None:
            if self.browser.current_window_handle != self.homePageHandle:
                self.browser.close()
            self.browser.switch_to.window(self.homePageHandle)
            pages = self.browser.find_elements_by_class_name('joblist-box__iteminfo.iteminfo')
            for page in pages:
                if page.get_property("href") == request.url:
                    page.click()
                    self.browser.switch_to.window(self.browser.window_handles[1])
                    time.sleep(self.loadTime)
                    page_text = self.browser.page_source
                    return HtmlResponse(url=self.browser.current_url, body=page_text, encoding='utf-8', request=request)
            raise Exception('找不到对应的网址a标签')
        elif request.meta.get('next_page') is not None:
            if self.browser.current_window_handle != self.homePageHandle:
                self.browser.close()
            self.browser.switch_to.window(self.homePageHandle)

            nextPageBtn = self.browser.find_elements_by_class_name('btn.soupager__btn')[1]
            nextPageBtn.click()
            time.sleep(self.loadTime)  # 给浏览器加载数据的时间
            page_text = self.browser.page_source
        else:
            if self.browser.current_window_handle != self.homePageHandle:
                self.browser.close()
            self.browser.switch_to.window(self.homePageHandle)
            self.browser.get(request.url)
            time.sleep(self.loadTime)  # 给浏览器加载数据的时间
            # 获取渲染后的数据
            page_text = self.browser.page_source
            # 篡改响应对象
        return HtmlResponse(url=self.browser.current_url, body=page_text, encoding='utf-8', request=request)
