from bs4 import BeautifulSoup
import requests
import os
from dropdown import get_tendaylists
global site_source
global soup
import subprocess
import sys
from signal import signal, SIGINT
from sys import exit
def handler(signal_received, frame):
    # Handle any cleanup here
    print('\nCTRL-C detected. Exiting program\n')
    exit(0)
signal(SIGINT, handler)
def clear():
    if os.name in ('nt','dos'):
        os.system("cls")
    elif os.name in ('linux','osx','posix'):
        os.system("clear")
class weatherTenDay:
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
        temperatures =[]
        description =[]
        avgindex =[]
        winddetails=[]
        for weather_Report in self.soup.find_all('summary', class_='Disclosure--Summary--AvowU DaypartDetails--Summary--2nJx1 Disclosure--hideBorderOnSummaryOpen--LEvZQ'):
            
            dateof_Report = weather_Report.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            

            temperature_day = weather_Report.find('div', class_='DetailsSummary--temperature--3FMlw').text
            

            weather_Description = weather_Report.find('div', class_='DetailsSummary--condition--mqdxh').text
            

            avg_precipindex = weather_Report.find('div', class_='DetailsSummary--precip--2ARnx').text
            

            wind_Details = weather_Report.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            
            
            dates.append(dateof_Report)
            temperatures.append(temperature_day)
            description.append(weather_Description)
            avgindex.append(avg_precipindex)
            winddetails.append(wind_Details)

    def weather_Details(self):
        weatherTenDay.weather_Deails(self)
        listnum = 0
        clear()
        print('''
                                                                | | | |                        | (_)
                                             __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                             \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                              \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                               \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

    ''')
        print('Date: ' + dates[listnum])
        print('Temperature: '+temperatures[listnum])
        print('Description: '+description[listnum])
        print('Precipitation Index: '+avgindex[listnum])
        print('Wind Details = '+ winddetails[listnum])
        inputs = input("Enter an option(n for next day and p for previous and e for extended info): ")
        while True:
            if inputs == 'n':
                clear()
                length = len(dates)
                listnum = listnum+1
                if listnum>13:
                    listnum = listnum-1
                    print('''
                                                                | | | |                        | (_)
                                             __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                             \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                              \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                               \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

    ''')
                    inputs = input('weather data not available after '+ dates[13]+ ', so please enter option again: :')
                else:
                    print('''
                                                                | | | |                        | (_)
                                             __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                             \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                              \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                               \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

    ''')
                    print('Date: ' + dates[listnum])
                    print('Temperature: '+temperatures[listnum])
                    print('Description: '+description[listnum])
                    print('Precipitation Index: '+avgindex[listnum])
                    print('Wind Details = '+ winddetails[listnum])
                    inputs = input("Enter an option(n for next day and p for previous and e for extended info): ")
            elif inputs == 'p':
                clear()
                dates[listnum]
                listnum = listnum-1
                if listnum<0:
                    print('''
                                                                | | | |                        | (_)
                                             __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                             \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                              \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                               \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

    ''')
                    listnum = listnum+1
                    inputs = input('weather data not available before '+ dates[0]+ ', so please enter option again:')
                else:
                    print('''
                                                                | | | |                        | (_)
                                             __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                             \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                              \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                               \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

    ''')
                    print('Date: ' + dates[listnum])
                    print('Temperature: '+temperatures[listnum])
                    print('Description: '+description[listnum])
                    print('Precipitation Index: '+avgindex[listnum])
                    print('Wind Details = '+ winddetails[listnum])
                    inputs = input("Enter an option(n for next day and p for previous and e for extended info): ")
            elif inputs == 'q':
                break
            elif inputs == 'e':
                get_tendaylists(self.site_source,listnum+1)
                inputs = input("Enter an option(n for next day and p for previous and e for extended info): ")
            else:
                print('''
                                                                | | | |                        | (_)
                                             __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                             \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                              \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                               \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

    ''')
                inputs = input('invalid option entered. please enter again(n for next day and p for previous and e for extended info): ')

                

