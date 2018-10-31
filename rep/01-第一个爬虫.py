from urllib.request import urlopen

url = "http://www.baidu.com/"
#发送请求
response = urlopen(url)
#读取内容
info = response.read()
#打印内容
print(info.decode())

#状态码
# code = response.getcode()
# print(code)
# #真实url
# urls = response.geturl()
# print(urls)
# #响应头
# info = response.info()
# print(info)