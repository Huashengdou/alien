import requests

# 执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&stars'
r = requests.get(url)

print("Start code:", r.status_code)

# 将响应的api存入一个变量中
response_dict = r.json()
print(response_dict.keys())