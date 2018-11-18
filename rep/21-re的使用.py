import re

str1 = "I Studey Python3.6 Everday"
print("------match()-------")
#匹配第一个字符
m1 = re.match(r'I',str1)
m2 = re.match(r'\w',str1)
m3 = re.match(r'.',str1)
m4 = re.match(r'\D',str1)
m5 = re.match(r'i',str1,re.I)
m6 = re.match(r'\S',str1)
#匹配Studey
m7 = re.match(r'Studey',str1) #匹配不到，因为match是从做开始匹配

print("------search()-------")
s1 = re.search(r'Studey',str1)
s2 = re.search(r'S\w+',str1)

#匹配Python3.6
s3 = re.search(r'P\w+.\d',str1)
print(s3.group())

print("------findall()-------")
f1 = re.findall(r'y',str1)
print(f1)


str2 = '<div><a herf="http://www.bjswt.com">尚学堂bjsxt</a></div>'

t1 = re.findall(r'[\u4e00-\u9fa5]\w+',str2)
t2 = re.findall(r'<a herf="http://www.bjswt.com">(.+)</a>',str2)
t3 = re.findall(r'<a herf="(.+)">',str2)
print(t2)
print(t3)

print("------sub()-------")
su1 = re.sub(r'<div>(.+)</div>',r'<span>\1</span>',str2)
print(su1)





