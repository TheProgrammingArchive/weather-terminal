from bs4 import BeautifulSoup
import requests

def get_tableToday(src):
    source = requests.get(src).text
    soup = BeautifulSoup(source, features='lxml')

    feels_like = soup.find('div', class_='TodayDetailsCard--hero--HySn3').text
    feels_like = feels_like[0:3]

    content_list = []

    for content in soup.find('div', class_='TodayDetailsCard--detailsContainer--1tqay'):
        content = content.text
        content_list.append(content)

    content_list.append(feels_like)
    return content_list



#rtcget = get_tableToday('https://weather.com/en-IN/weather/today/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c')
#print(rtcget)
