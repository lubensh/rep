import json

str = '{"name":"盗梦空间"}'
# 字符串转json
obj = json.loads(str)
print(obj)
# json转字符串
str2 = json.dumps(obj, ensure_ascii=False)
print(str2)
# 转成文件
json.dump(obj, open("movie.txt", "w", encoding="utf-8"), ensure_ascii=False)
# 读取文件
str3 = json.load(open("movie.txt", encoding="utf-8"))
print(str3)
