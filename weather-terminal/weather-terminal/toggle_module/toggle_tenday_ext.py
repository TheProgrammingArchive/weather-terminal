from bs4 import BeautifulSoup
import requests
import os
import toggle_module
from toggle_module import toggle_drpdw, toggle_tenday_ext
global site_source
global soup
import shutil
import subprocess
import sys
from signal import signal, SIGINT
from sys import exit


def title():
    title_content = '''
                     _   _                      _                                    _ 
                    | | | |                    | |                    (_)           | |
 __      _____  __ _| |_| |__   ___ _ __ ______| |_ ___ _ __ _ __ ___  _ _ __   __ _| |
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______| __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
  \ V  V /  __/ (_| | |_| | | |  __/ |         | ||  __/ |  | | | | | | | | | | (_| | |
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|          \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                                                                       
                        '''
    for shutter_title in title_content.split('\n'):
        print(shutter_title.center(shutil.get_terminal_size().columns))


def handler(signal_received, frame):
    # Handle any cleanup here
    exit(0)


signal(SIGINT, handler)


def clear():
    if os.name in ('nt', 'dos'):
        os.system("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        os.system("clear")


class weatherTenDay_toggle_dble:
    def __init__(self, site_source):
        self.site_source = site_source
        self.src = requests.get(self.site_source).text
        self.soup = BeautifulSoup(self.src, features='lxml')

    def timeof_report(self):
        global time
        time = self.soup.find('div', class_='DailyForecast--timestamp--iI022').text

    def weather_Deails(self):
        global dates
        global temperatures
        global description
        global avgindex
        global winddetails
        dates = []
        temperatures = []
        description = []
        avgindex = []
        winddetails = []
        for weather_Report in self.soup.find_all('summary',
                                                 class_='Disclosure--Summary--AvowU DaypartDetails--Summary--2nJx1 Disclosure--hideBorderOnSummaryOpen--LEvZQ'):
            dateof_Report = weather_Report.find('h2', class_='DetailsSummary--daypartName--1Mebr').text

            temperature_day = weather_Report.find('div', class_='DetailsSummary--temperature--3FMlw').text

            weather_Description = weather_Report.find('div', class_='DetailsSummary--condition--mqdxh').text

            avg_precipindex = weather_Report.find('div', class_='DetailsSummary--precip--2ARnx').text

            wind_Details = weather_Report.find('div',
                                               class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text

            dates.append(dateof_Report)
            temperatures.append(temperature_day)
            description.append(weather_Description)
            avgindex.append(avg_precipindex)
            winddetails.append(wind_Details)

    def weather_Details(self):
        clear()
        weatherTenDay_toggle_dble.weather_Deails(self)
        listnum = 0
        #title
        title()

        print('\n\nWhen asked >> press N for next day and P for previous day, E for more weather info or Q to exit\n\n')

        print('Date: ' + dates[listnum])
        print('Temperature: ' + temperatures[listnum])
        print('Description: ' + description[listnum])
        print('Precipitation Index: ' + avgindex[listnum])
        print('Wind Details = ' + winddetails[listnum])
        print()
        print('Extended Information: ')
        print()
        toggle_drpdw.get_tendaylists(self.site_source, listnum + 1)
        inputs = input("\n\n>>  ")
        while True:
            if inputs.upper() == 'N':
                clear()
                length = len(dates)
                listnum = listnum + 1
                if listnum > 11:
                    listnum = listnum - 1
                    #title
                    title()
                    inputs = input(f'Data unavailable after {dates[11]}. You can go back(P) or Q(EXIT)>> ')
                else:
                    #title
                    title()
                    print('Date: ' + dates[listnum])
                    print('Temperature: ' + temperatures[listnum])
                    print('Description: ' + description[listnum])
                    print('Precipitation Index: ' + avgindex[listnum])
                    print('Wind Details = ' + winddetails[listnum])
                    print()
                    print('Extended Information: ')
                    print()
                    toggle_drpdw.get_tendaylists(self.site_source, listnum + 1)
                    inputs = input(">> ")
            elif inputs.upper() == 'P':
                clear()
                dates[listnum]
                listnum = listnum - 1
                if listnum < 0:
                    #title
                    title()
                    listnum = listnum + 1
                    inputs = input(f'Weather data unavailable before {dates[0]}. You can go forward(N) or Q(EXIT)!>> ')
                else:
                    #title
                    title()
                    print('Date: ' + dates[listnum])
                    print('Temperature: ' + temperatures[listnum])
                    print('Description: ' + description[listnum])
                    print('Precipitation Index: ' + avgindex[listnum])
                    print('Wind Details = ' + winddetails[listnum])
                    print()
                    print('Extended Information: ')
                    print()
                    toggle_drpdw.get_tendaylists(self.site_source, listnum + 1)
                    inputs = input(">>")
            elif inputs.upper() == 'Q':
                break
            else:
                #title
                inputs = input('>> ')
