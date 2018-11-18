import requests
from fake_useragent import UserAgent

#get请求
headers = {
    "User-Agent": UserAgent().chrome
}

url = "https://www.sxt.cn/index/login/login.html"
form__data = {
    "user": "17703181473",
    "password": "123456"
}
response = requests.post(url,headers=headers,data=form__data)
print(response.text)