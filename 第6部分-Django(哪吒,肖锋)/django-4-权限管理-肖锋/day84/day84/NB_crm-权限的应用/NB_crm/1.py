
import requests_html
url = 'http://pic.netbian.com/'

session = requests_html.HTMLSession()

res = session.get('http://pic.netbian.com/')
res.html.render()
# s = res.html.find('img')
# for item in s:
#     print(item.attrs.get('src'))

print(res.html.absolute_links)