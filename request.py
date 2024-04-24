import requests
import re


a = input()
b = input()

all_links = []
site = requests.get(a).text
links = re.findall(r'href=[\"\'](.*?)[\"\']', site)

for link in links:
    html = requests.get(link.replace('stepic.org','stepik.org')).text
    html = html.replace('stepic.org','stepik.org')
    cycle_sites = re.findall(r'href=[\"\'](.*?)[\"\']', html)
    list(map(lambda x: x.replace('stepic.org', 'stepik.org'), cycle_sites))
    all_links.extend(cycle_sites)

if b in all_links:
    print('Yes')
else:
    print('No')