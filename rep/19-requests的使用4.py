from fake_useragent import UserAgent
import requests

url = "https://www.12306.cn/mormhweb/"
headers = {
    "User-Agent": UserAgent().chrome
}
#禁用安全请求警告
requests.packages.urllib3.disable_warnings()

response =requests.get(url,verify = False,headers=headers)
response.encoding="utf-8"
print(response.text)