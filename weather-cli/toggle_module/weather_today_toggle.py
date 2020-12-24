from bs4 import BeautifulSoup
import shutil
import requests
import os

def title():
    title_content = '''
                    | | | |                        | (_)
 __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
  \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

                    '''
    for shutter_title in title_content.split('\n'):
        print(shutter_title.center(shutil.get_terminal_size().columns))

def clear():
    if os.name in ('nt', 'dos'):
        os.system("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        os.system("clear")

class WeatherToggleHourly:
    def __init__(self, src):
        self.src = src
        self.source = requests.get(src).text
        self.soup = BeautifulSoup(self.source, features='lxml')

    def get_hrlcontent(self):
        time_list = []
        tm_list = []
        dsc_list = []
        pr_list = []
        wspeed_list = []

        for reports in self.soup.find_all('details', class_='DaypartDetails--DayPartDetail--3yhtR Disclosure--themeList--uBa5q'):

            timeofreport = reports.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            # print(f"Time of update: {timeofreport}")

            temperature_now = reports.find('div', class_='DetailsSummary--temperature--3FMlw').text
            # print(f"Temperature: {temperature_Now}")

            weather_description = reports.find('div', class_='DetailsSummary--condition--mqdxh').text
            # print(f"Description: {weather_description}")

            precip_index = reports.find('div', class_='DetailsSummary--precip--2ARnx').text
            # print(f"Precipitation Index: {precip_index}")

            wind_speed = reports.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            # print(f"Wind speed: {wind_speed}")

            time_list.append(timeofreport)
            tm_list.append(temperature_now)
            dsc_list.append(weather_description)
            pr_list.append(precip_index)
            wspeed_list.append(wind_speed)

            if timeofreport >= '23:00':
                break
            else:
                continue

        return time_list, tm_list, dsc_list, pr_list, wspeed_list

    def get_togglehrhr(self):
        content_values = WeatherToggleHourly.get_hrlcontent(self)
        time_content = content_values[0]
        tm_content = content_values[1]
        dsc_content = content_values[2]
        precip_content = content_values[3]
        wspeed_content = content_values[4]

        list_lent = len(time_content)
        list_index = 0

        clear()
        title()

        print('\nWhen asked >> Press (N) to view next hour, (P) to view previous hour, (Q) to quit\n')

        print(f'Time of update: {time_content[0]}')
        print(f'Temperature: {tm_content[0]}')
        print(f'Description: {dsc_content[0]}')
        print(f'Precipitation: {precip_content[0]}')
        print(f'Windspeed: {wspeed_content[0]}')

        while True:
            fwd_value = input('>> ')
            if fwd_value.upper() == 'N':
                clear()
                title()
                list_index = list_index + 1

                if list_index == list_lent:
                    print(f'Data unavailable after {time_content[list_index-1]}, view previous hour (P) or Quit(Q)')
                    list_index = list_lent - 1

                else:
                    print(f'Time of update: {time_content[list_index]}')
                    print(f'Temperature: {tm_content[list_index]}')
                    print(f'Description: {dsc_content[list_index]}')
                    print(f'Precipitation: {precip_content[list_index]}')
                    print(f'Windspeed: {wspeed_content[list_index]}')

            elif fwd_value.upper() == 'P':
                clear()
                title()
                list_index = list_index - 1

                if list_index < 0:
                    print(f'Data unavailable before {time_content[0]}, view next hour (N) or Quit(Q)')
                    list_index = 0

                else:
                    print(f'Time of update: {time_content[list_index]}')
                    print(f'Temperature: {tm_content[list_index]}')
                    print(f'Description: {dsc_content[list_index]}')
                    print(f'Precipitation: {precip_content[list_index]}')
                    print(f'Windspeed: {wspeed_content[list_index]}')

            elif fwd_value.upper() == 'Q':
                break

            else:
                continue

# new_content = WeatherToggleHourly('https://weather.com/en-IN/weather/hourbyhour/l/db1e2342716e8c57c40b728ac1c43ce012289a41d1c10de9a76ba1777a8de974')
# new_content.get_togglehrhr()