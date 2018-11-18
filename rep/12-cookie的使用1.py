from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "https://www.sxt.cn/index/user.html"

headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie":"PHPSESSID=d1u770jlh18p2oa1p0f846lvs1; UM_distinctid=166cf96386c64e-0c127d513bd633-47e1137-1fa400-166cf96386d55b; CNZZDATA1261969808=1793673706-1541076025-https%253A%252F%252Fwww.sxt.cn%252F%7C1541076025; 53gid2=10296284183012; visitor_type=new; 53gid0=10296284183012; 53gid1=10296284183012; 53revisit=1541081021135; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_keyword=https%3A%2F%2Fwww.sxt.cn%2Findex%2Flogin%2Flogin.html; 53kf_72085067_land_page=https%253A%252F%252Fwww.sxt.cn%252Findex.html; kf_72085067_land_page_ok=1"
}

request = Request(url, headers=headers)
response = urlopen(request)
info = response.read().decode()
print(info)
