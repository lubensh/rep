from threading import Thread
from queue import Queue
import requests
from fake_useragent import UserAgent
from lxml import etree


# 爬虫类
class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().random
        }
        while self.url_queue.empty() == False:
            response = requests.get(self.url_queue.get(), headers=headers)
            if response.status_code == 200:
                self.html_queue.put(response.text)


# 解析类
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while self.html_queue.empty() == False:
            e = etree.HTML(self.html_queue.get())
            span_content = e.xpath('//div[@class="content"]/span[1]')
            with open("duanzi28.txt","a",encoding="utf-8") as f:
                for span in span_content:
                    info = span.xpath('string(.)')
                    f.write(info +'\n')


if __name__ == '__main__':
    # 存储url的容器
    url_queue = Queue()
    # 存储内容的容器
    html_queue = Queue()
    base_url = "https://www.qiushibaike.com/text/page/{}/";
    for i in range(1, 14):
        new_url = base_url.format(i)
        url_queue.put(new_url)
    crawl_list = []
    for i in range(0, 3):
        # 创建一个爬虫
        crawl = CrawlInfo(url_queue, html_queue)
        crawl_list.append(crawl)
        crawl.start()
    for crawl in crawl_list:
        crawl.join()
    parse_list = []
    for i in range(0, 3):
        #创建一个解析
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    for parse in parse_list:
        parse.join()