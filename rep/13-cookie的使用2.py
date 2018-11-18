from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor,build_opener

# 登录
login_url = "https://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
from_data = {
    "user": "17703181473",
    "password": "123456"
}
f_data = urlencode(from_data).encode()
request = Request(login_url, headers=headers,data = f_data)
#response = urlopen(request)
handler = HTTPCookieProcessor()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
# 访问页面
info_url = "https://www.sxt.cn/index/user.html"
request = Request(info_url, headers=headers)
#response = urlopen(request)
response = opener.open(request)
info = response.read().decode()
print(info)
