from bs4 import BeautifulSoup
import requests
global soup
global source
source = requests.get('https://weather.com/en-SG/weather/today/l/SNXX0006:1:SN?Goto=Redirected').text

soup = BeautifulSoup(source, 'lxml')
links = soup.find('a', class_='ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ')
links5 = str(links)
links1 =links5.replace('<a class="ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ" data-from-string="localsuiteNav_2_Hourly" href="', "")
link3 = links1.replace('" target="_self"><span class="styles--liContent--1nCd7">Hourly</span></a>', "")
finallink= "https://weather.com"+link3
print(finallink)

