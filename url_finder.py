from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
global soup
global source
#replace the url with any non english or english url and it shall work yayaayy
source = requests.get('https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW').text

soup = BeautifulSoup(source, 'lxml')
links = soup.find('a', class_='ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ')
links5 = str(links)
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag. very yes 
        if tag == "a":
           # Check the list of defined attributes. just yes
           for name, value in attrs:
               # If href is defined, print it. yes
               if name == "href":
                   print("https://weather.com"+value)


parser = MyHTMLParser()
parser.feed(links5)
