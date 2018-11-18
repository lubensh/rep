from urllib.request import Request,build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url ="http://httpbin.org/get"
headers = {
    "User-Agent":UserAgent().chrome
}
request = Request(url,headers = headers)
handler = ProxyHandler({"http":"221.7.255.168:8080"})
#handler = ProxyHandler({"http":"username:password&ip:port"})
opener = build_opener(handler)
response = opener.open(request)
info = response.read().decode()
print(info)