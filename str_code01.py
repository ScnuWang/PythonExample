import requests

print(requests.get('http://you.163.com/item/list?categoryId=1005000&_stat_area=nav_2&_stat_referer=index').text)