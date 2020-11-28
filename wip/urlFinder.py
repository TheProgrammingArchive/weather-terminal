from url_Grabber import get_input
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
r = requests.get("https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW?Goto=Redirected")
# the below line has been commented cuz its optional and mostly not needed.
# r2 = requests.get('https://weather.com/hr-HR/weather/today/l/TWXX0021:1:TW?Goto=Redirected')
# replace de-DE in the below link with appropriate locale (https://saimana.com/list-of-country-locale-code/) and get url

locale = input('Location code: ')

source = f'https://weather.com/{locale}'

r3 = requests.get(source)

#replace the url with any non english or english url and it shall work yayaayy

source2 = requests.get(r3).text

soup = BeautifulSoup(source2, features='lxml')
links = soup.find('a', class_='ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ')
links5 = str(links)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag. very yes
        if tag == "a":
           # Check the list of defined attributes. just ye
            if name == "href":
                   return ("https://weather.com"+value)

try:
    parser = MyHTMLParser().handle_starttag()
except requests.exceptions.InvalidURL:
    print(parser.feed(links5))
