import requests
import re
from fake_useragent import UserAgent

url = "https://www.qiushibaike.com/text/page/1/"
headers = {
    "User-Agent": UserAgent().random
}

#构造请求
response = requests.get(url,headers=headers)
info = response.text

infos = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>',info)
print(infos)

with open('duanzi22.txt','w',encoding='utf-8') as f:
    for info in infos:
        f.write(info + "\n\n\n")