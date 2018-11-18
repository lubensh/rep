from fake_useragent import UserAgent
import requests

url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().chrome
}
proxies = {
    "http":"http://221.7.255.168:8080"
}
response =requests.get(url,headers=headers,proxies=proxies)
print(response.text)