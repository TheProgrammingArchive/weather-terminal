import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
r = requests.get("https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW?Goto=Redirected")
#the below line has been commented cuz its optional and mostly not needed.
#r2 = requests.get('https://weather.com/hr-HR/weather/today/l/TWXX0021:1:TW?Goto=Redirected')
#replace de-DE in the below link with appropriate locale(https://saimana.com/list-of-country-locale-code/) and get url
r3 = requests.get("https://weather.com/en-IN/").text
source = r3
soup = BeautifulSoup(source, 'lxml')
links = soup.find('a', class_='ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ')
links5 = str(links)
soup = BeautifulSoup(links5, "html.parser")
for links5 in soup.findAll('a'):
    x = 'https://weather.com'+links5.get('href')
    print(x)

