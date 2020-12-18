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
                    humiditycurrent.append(table_content[8:11])

                elif (i == 1):
                    # print(f'UV Index (Currently): {table_content[8:20]}')
                    uvindexcurrent.append(table_content[8:20])
                elif (i == 2):
                    # print(table_content)
                    sunrise.append(table_content[7:])
                elif (i == 3):

                    # print(table_content)
                    sunset.append(table_content[6:])

                elif (i == 4):
                    # print(f'Humidity (Later): {table_content[8:20]}')
                    humiditylater.append(table_content[8:20])

                elif (i == 5):
                    # print(f'UV Index (Later): {table_content[8:20]}')
                    uvindexlater.append(table_content[8:20])

                elif (i == 6):
                    # print(table_content)
                    moonrise.append(table_content[8:])
                elif (i == 7):
                    # print(table_content)
                    moonset.append(table_content[7:])
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
    print('Description (Currently): ' + descriptioncurrent[listnum])
    print('Description (Later): ' + descriptionlater[listnum])
    print()
    print('Humidity (Currently): ' + humiditycurrent[listnum])
    print('UV Index (Currently): ' + uvindexcurrent[listnum])
    print('Sunrise: ' + sunrise[listnum])
    print('Sunset: ' + sunset[listnum])
    print()
    print('Humidity (Later): ' + humiditylater[listnum])
    print('UV Index (Later): ' + uvindexlater[listnum])
    print('Moonrise: ' + moonrise[listnum])
    print('Moonset: ' + moonset[listnum])
    print()

