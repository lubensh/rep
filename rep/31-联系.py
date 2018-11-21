import requests
from fake_useragent import UserAgent
from lxml import etree

url = 'http://www.farmer.com.cn/jjpd/nz/nzdt/201811/t20181116_1417204.htm'
headers = {
    "User-Agent": UserAgent().chrome
}

response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
title = e.xpath('//h1/text()')
all_p_tag = e.xpath("//div[@class='content']//p")
content = []
for p in all_p_tag:
    info = p.xpath('string(.)')
    content.append(info)
content_str = ''.join(content)
img_urls = e.xpath("//div[@class='content']//img/@src")
img_names = e.xpath("//div[@class='content']//p/font")
img_all_name = []
for img_name in img_names:
    img_name = img_name.xpath('string(.)')
    img_all_name.append(title[0] + img_name)

