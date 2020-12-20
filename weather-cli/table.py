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
    valuetemp = 'High/Low: '+content_list[0][-7:]
    wind = 'Wind: '+content_list[1][-6:]
    humiditye = 'Humidity: '+content_list[2][-3:]
    dewpointe = 'Dew point: '+content_list[3][-3:]
    pressuree = 'Pressure: '+content_list[4][-9:]
    uvindexe = 'UV Index: ' +content_list[5][-7:]
    visi = 'Visibility: '+content_list[6][-7:]
    lemoon = content_list[7]
    moonphse = 'Moon phase: '+lemoon.replace(content_list[7][0:10],'')
    listfinal = [valuetemp,wind,humiditye,dewpointe,pressuree,uvindexe,visi,moonphse]
    return listfinal


#rtcget = get_tableToday('https://weather.com/en-IN/weather/today/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c')
#print(rtcget)
