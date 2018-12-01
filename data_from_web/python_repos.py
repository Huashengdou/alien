import requests

# 执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&stars'
r = requests.get(url)

print("Start code:", r.status_code)

# 将响应的api存入一个变量中
response_dict = r.json()
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])
# 获取有关仓库信息
repo_dicts = response_dict['items']
print('repositories returned:',len(repo_dicts))
# 研究第一个仓库
repo_dict = repo_dicts[0]
#for key in sorted(repo_dict.keys()):
#   print(key)

print("\nSelected information about first repository:")
print('Name:',repo_dict['name'])
print('Owener:',repo_dict['owner']['login'])
print('Starts:',repo_dict['stargazers_count'])
print('Repository:',repo_dict['html_url'])
print('Created:',repo_dict['created_at'])
print('Updated:',repo_dict['updated_at'])
print('Description:',repo_dict['description'])
