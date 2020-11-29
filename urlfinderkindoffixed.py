import requests
from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser
locationcode = input("Enter the location code(from weather.codes):")

source = requests.get('https://weather.com/en-SG/weather/today/l/'+locationcode).text

soup = BeautifulSoup(source, 'lxml')
links = soup.find('a', class_='ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ')
links5 = str(links)
soup = BeautifulSoup(links5, "html.parser")
for links5 in soup.findAll('a'):
    x = 'https://weather.com'+links5.get('href')
    print(x)

