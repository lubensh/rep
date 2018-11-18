from urllib.request import Request, build_opener, HTTPCookieProcessor
from fake_useragent import UserAgent
from http.cookiejar import MozillaCookieJar
from urllib.parse import urlencode

def get_cookie():
    login_url = "https://www.sxt.cn/index/login/login"
    headers = {
        "User-Agent": UserAgent().chrome
    }
    form_data = {
        "user": "17703181473",
        "password": "123456"
    }
    f_data= urlencode(form_data).encode()
    request = Request(login_url, headers=headers,data=f_data)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save("cookie.txt", ignore_expires=True, ignore_discard=True)


def user_cookie():
    info_url = "https://www.sxt.cn/index/user.html"
    headers = {
        "User-Agent": UserAgent().chrome
    }
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load("cookie.txt",ignore_discard=True,ignore_expires=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    print(response.read().decode())


if __name__ == '__main__':
    #get_cookie()
    user_cookie()
