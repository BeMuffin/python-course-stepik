#https://stepik.org/lesson/24471/step/7?discussion=370591&unit=6780 - stepik task 
#3.3 Обзорно об интернете: http-запросы, html-страницы и requests

import requests
import re



input_link = input()

site = requests.get(input_link).text

all_sites = []
sites = re.findall(r'(?:<a.+?href=(?:[\'\"])?)(?!.*\.\.\/)(?:https?:\/\/)?(?:ftp?:\/\/)?([\w\-\.]+)', site)
for site in sites:
    if site not in all_sites:  
        all_sites.append(site)

all_sites.sort()
for site in all_sites:
    print (site)
