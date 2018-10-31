from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = "http://www.baidu.com/"

user_agents = ["Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
               "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"]
#print(choice(user_agents))
headers = {
    "User-Agent":choice(user_agents)
}
request = Request(url,headers=headers)
#print(request.get_header('User-agent'))
#发送请求
response = urlopen(request)
#读取内容
info = response.read()
#打印内容
print(info.decode())