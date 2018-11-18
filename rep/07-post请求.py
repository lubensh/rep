from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

url = "https://www.sxt.cn/index/login/login.html"
form__data = {
    "user": "17703181473",
    "password": "123456"
}
headers = {
    "User-Agent": UserAgent().chrome
}
f_data = urlencode(form__data)
request = Request(url, data=f_data.encode(), headers=headers)
response = urlopen(request)
print(response.read().decode())
