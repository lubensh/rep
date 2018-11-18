from fake_useragent import UserAgent
import requests

session = requests.Session()
login_url = "https://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
form_data = {
    "user": "17703181473",
    "password": "123456"
}
response = session.post(login_url, headers=headers, data=form_data)
info_url = "https://www.sxt.cn/index/user.html"
resp = session.get(info_url, headers=headers)
print(resp.text)
