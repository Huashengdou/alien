import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&stars'
r = requests.get(url)

print("Start code:", r.status_code)

# 将响应的api存入一个变量中
response_dict = r.json()
#print(response_dict.keys())
#print("Total repositories:", response_dict['total_count'])
# 获取有关仓库信息
repo_dicts = response_dict['items']
names, stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 14
my_config.label_font_size = 30
my_config.major_label_font_size = 18
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svq')
"""
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
"""
