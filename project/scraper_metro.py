
import requests
from bs4 import BeautifulSoup as bs

URL = "http://metroalmaty.kz/?q=ru/schedule-list"

page = requests.get(URL)
soup = bs(page.text, "html.parser")
data = []
for i in soup.find_all("td"):
    td = i.get_text()
    data.append(td)



stations = data[::3]
print(stations)

'''
stations_name = []
for item in data[::3]:
    stations_name.append(item)
'''

time_rayymbek_momyshuly = data[1::3]
print(time_rayymbek_momyshuly)

'''
rayymbek_momyshuly = []
for item in data[1::3]:
    rayymbek_momyshuly.append(item)
rayymbek_momyshuly
'''

time_momyshuly_rayymbek = data[2::3]
print(time_momyshuly_rayymbek)

'''
momyshuly_rayymbek = []
for item in data[2::3]:
    momyshuly_rayymbek.append(item)
momyshuly_rayymbek
'''



