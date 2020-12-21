from bs4 import BeautifulSoup
import requests
from weather_today import weatherHourly
import csv
import art
import os
import shutil
import tableprint
import sys
class weatherHoury:
    def __init__(self, source):
        self.source = source
        self.src = requests.get(self.source).text
        self.soup = BeautifulSoup(self.src, features='lxml')
        self.weather_now = self.soup.find('div', class_='DaypartDetails--DetailSummaryContent--1c28m Disclosure--SummaryDefault--1z_mF')
    def getHourlyweather(self):
        global time
        global temp
        global desc
        global precip
        global wind
        time = []
        temp = []
        desc = []
        precip = []
        wind = []
        for reports in self.soup.find_all('details', class_='DaypartDetails--DayPartDetail--3yhtR Disclosure--themeList--uBa5q'):
            timeofreport = reports.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            #print(f"Time: {timeofreport}")

            temperature_Now = reports.find('div', class_='DetailsSummary--temperature--3FMlw').text
            #print(f"Temperature: {temperature_Now}")

            weather_description = reports.find('div', class_='DetailsSummary--condition--mqdxh').text
            #print(f"Description: {weather_description}")

            precip_index = reports.find('div', class_='DetailsSummary--precip--2ARnx').text
            #print(f"Precipitation Index: {precip_index}")

            wind_speed = reports.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            #print(f"Wind speed: {wind_speed}")
            #print('\n\n----------------------------------------------------------------------------------------\n',end='|')
            time.append(timeofreport)
            temp.append(temperature_Now)
            desc.append(weather_description)
            precip.append('Precipitation: '+precip_index)
            wind.append('Wind: ' + wind_speed)
            if(timeofreport >= '23:00'):
                break
            else:
                continue
            
    def weather_atThisHour(self):
        location = weatherHourly(self.source)
        location = location.location_m()
        print(location.center(os.get_terminal_size().columns))
        time_now = self.weather_now.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
        temperature_current = self.weather_now.find('div', class_='DetailsSummary--temperature--3FMlw').text
        #print(temperature_current.center(os.get_terminal_size().columns))
        s=art.text2art(temperature_current+'  c','standard')
        for line in s.split("\n"):
            print(line.center(shutil.get_terminal_size().columns))
        weatherdesc_current = self.weather_now.find('div', class_='DetailsSummary--condition--mqdxh').text
        print(weatherdesc_current.center(os.get_terminal_size().columns))
        time_now = 'Updated as of '+ self.weather_now.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
        print(time_now.center(os.get_terminal_size().columns))
        a_string = "-"
        width = os.get_terminal_size().columns
        n=0
        stringman = ''
        while n<=width:
            stringman = stringman+a_string
            n=n+1
        print(stringman)
        print()
        print('Hourly Weather')

        weatherHoury.getHourlyweather(self)
        
        fitnumcolumns = width/20
        intcolumnsfit = int(fitnumcolumns)
        
        fittime = time[0:intcolumnsfit]
        fittemp = temp[0:intcolumnsfit]
        fitdesc = desc[0:intcolumnsfit]
        fitprecip = precip[0:intcolumnsfit]
        fitwind = wind[0:intcolumnsfit]
        lengthlist = len(fittime)
        rowlist = width/lengthlist-3
        introwlength = int(rowlist)
        if fitnumcolumns == lengthlist:
            print(tableprint.row(fittime, width=introwlength, format_spec='5g', style='round'))
            print(tableprint.row(fittemp, width=introwlength, format_spec='5g', style='round'))
            print(tableprint.row(fitdesc, width=introwlength, format_spec='5g', style='round'))
            print(tableprint.row(fitprecip, width=introwlength, format_spec='5g', style='round'))
            print(tableprint.row(fitwind, width=introwlength, format_spec='5g', style='round'))
        else:
            print(tableprint.row(fittime, width=introwlength, format_spec='5g', style='round'))
            print(tableprint.row(fittemp, width=introwlength, format_spec='5g', style='round'))
            print(tableprint.row(fitdesc, width=introwlength, format_spec='5g', style='round')+'')
            print(tableprint.row(fitprecip, width=introwlength, format_spec='5g', style='round'))
            print(tableprint.row(fitwind, width=introwlength, format_spec='5g', style='round'))
            
