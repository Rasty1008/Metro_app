
import requests
from bs4 import BeautifulSoup as bs


URL = "http://metroalmaty.kz/?q=ru/schedule-list"

page = requests.get(URL)
soup = bs(page.text, "html.parser")
data = ""
for i in soup.find_all("td"):
    td = i.get_text()
    data = f"{data} {td}"

print(data)
'''
def time_stations(data):
    time = []
    for i in data:
        i = i.replace(":", "")
        if i.isdigit():
            time.append(i)
    return time
print(time_stations(data)
'''


