from bs4 import BeautifulSoup
import requests
import time
import sys


def get_tendeyweather(source):
    global datetime
    global maxtemp
    global mintemp
    global descriptioncurrent
    global descriptionlater
    global humiditycurrent
    global uvindexcurrent
    global uvindexlater
    global humiditylater
    global sunrise
    global sunset
    global moonrise
    global moonset
    datetime = []
    maxtemp = []
    mintemp = []
    descriptioncurrent = []
    descriptionlater = []
    humiditycurrent = []
    uvindexcurrent = []
    uvindexlater = []
    humiditylater = []
    sunrise = []
    sunset = []
    moonrise = []
    moonset = []

    site_source = requests.get(source).text
    soup = BeautifulSoup(site_source, features='lxml')

    for dropdown_article in soup.find_all('div',
                                          class_='DaypartDetails--Content--XQooU DaypartDetails--contentGrid--3cYKg'):
        gochar = None
        # print(dropdown_article)
        i = 0
        for date_time in dropdown_article.find_all('h3', class_='DailyContent--daypartName--3G5Y8'):

            date_time = date_time.text
            if (i == 0):
                # print(date_time[0:7])
                datetime.append(date_time[0:7])
            else:
                break
            i = i + 1

        i = 0
        # print()
        for temp_morning in dropdown_article.find_all('span', class_='DailyContent--temp--_8DL5'):
            temp_morning = temp_morning.text
            if (i == 0):
                # print(f'Maximum Temperature: {temp_morning}')
                maxtemp.append(temp_morning)
            else:
                # print(f'Minimum Temperature: {temp_morning}')
                mintemp.append(temp_morning)
            i = i + 1

        i = 0
        # print()
        for weather_desc in dropdown_article.find_all('p', class_='DailyContent--narrative--3AcXd'):
            weather_desc = weather_desc.text
            if (i == 0):
                # print(f'Description (Currently): {weather_desc}')
                descriptioncurrent.append(weather_desc)
            else:
                # print(f'Description (Later): {weather_desc}')
                descriptionlater.append(weather_desc)
            i = i + 1

        i = 0
        # print()
        for details in dropdown_article.find_all('ul',
                                                 class_='DetailsTable--DetailsTable--2qH8C DaypartDetails--DetailsTable--2fwt-'):
            for table_content in details.find_all('li', class_='DetailsTable--listItem--1MW7X'):
                table_content = table_content.text
                if (i == 0):
                    # print(f'Humidity (Currently): {table_content[8:11]}')
                    table_content = table_content.replace('Humidity', '')
                    humiditycurrent.append(table_content)

                elif (i == 1):
                    # print(f'UV Index (Currently): {table_content[8:20]}')
                    table_content = table_content.replace('UV LevelUV Index', '')
                    uvindexcurrent.append(table_content)

                elif (i == 2):
                    # print(table_content)
                    table_content = table_content.replace('Sun RiseSunrise', '')
                    sunrise.append(table_content)

                elif (i == 3):
                    # print(table_content)
                    table_content = table_content.replace('Sunset', '')
                    sunset.append(table_content)

                elif (i == 4):
                    # print(f'Humidity (Later): {table_content[8:20]}')
                    table_content = table_content.replace('Humidity', '')
                    humiditylater.append(table_content)

                elif (i == 5):
                    # print(f'UV Index (Later): {table_content[8:20]}')
                    table_content = table_content.replace('UV LevelUV Index', '')
                    uvindexlater.append(table_content)

                elif (i == 6):
                    # print(table_content)
                    table_content = table_content.replace('Moon RiseMoonrise', '')
                    table_content = table_content[0:5]
                    
                    if table_content == '--Moo':
                        moonrise.append('--')

                    else:
                        moonrise.append(table_content)

                elif (i == 7):
                    # print(table_content)
                    table_content = table_content.replace('Moon SetMoonset', '')
                    moonset.append(table_content)
                i = i + 1

        # gochar = input('\n>>')
        # if gochar.lower() == 'q':
        # break
        # else:
        # continue
        # print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')


def get_tendaylists(sourcem, listnum):
    get_tendeyweather(sourcem)
    print()
    print('Date: ' + datetime[listnum])
    print()
    print('Maximum Temperature: ' + maxtemp[listnum])
    print('Minimum Temperature: ' + mintemp[listnum])
    print()
    print('Description (Morning): ' + descriptioncurrent[listnum])
    print('Description (Night): ' + descriptionlater[listnum])
    print()
    print('Humidity (Morning): ' + humiditycurrent[listnum])
    print('UV Index (Morning): ' + uvindexcurrent[listnum])
    print('Sunrise: ' + sunrise[listnum])
    print('Sunset: ' + sunset[listnum])
    print()
    print('UV Index (Night): ' + uvindexlater[listnum])

    src = requests.get(sourcem).text

    soup = BeautifulSoup(src, features='lxml')
    time = soup.find('div', class_='DailyForecast--timestamp--iI022')
    time = time.text
    time = time[6:11]

    time = time.replace(':', '.')

    time = float(time)

    if (time >= 15.21):
        print('Humidity (Night): ' + humiditylater[listnum-1])
        print('Moonrise: ' + moonrise[listnum-1])
        print('Moonset: ' + moonset[listnum-1])

    else:
        print('Humidity (Night): ' + humiditylater[listnum])
        print('Moonrise: ' + moonrise[listnum])
        print('Moonset: ' + moonset[listnum])
    print()

