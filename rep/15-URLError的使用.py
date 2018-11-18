from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

url = "https://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
try:
    req = Request(url, headers=headers)
    resp = urlopen(req)
    print(resp.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args[0].errno)
    print(e)