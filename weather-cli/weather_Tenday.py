from bs4 import BeautifulSoup
import requests
#temporary source
global site_source
global soup
class weatherTenDay:
    def __init__(self, site_source):
        self.site_source = site_source
        self.src = requests.get(self.site_source).text
        self.soup = BeautifulSoup(self.src, features='lxml')
    def timeof_report(self):
        time = self.soup.find('div', class_='DailyForecast--timestamp--iI022').text
        print(time)
    def weather_Details(self):
        for weather_Report in self.soup.find_all('summary', class_='Disclosure--Summary--AvowU DaypartDetails--Summary--2nJx1 Disclosure--hideBorderOnSummaryOpen--LEvZQ'):
            dateof_Report = weather_Report.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            print(f"Date: {dateof_Report}")
            temperature_day = weather_Report.find('div', class_='DetailsSummary--temperature--3FMlw').text
            print(f"Temperature: {temperature_day}")
            weather_Description = weather_Report.find('div', class_='DetailsSummary--condition--mqdxh').text
            print(f"Description: {weather_Description}")
            avg_precipindex = weather_Report.find('div', class_='DetailsSummary--precip--2ARnx').text
            print(f"Precipitation Index: {avg_precipindex}")
            wind_Details = weather_Report.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            print(f"Wind Details = {wind_Details}")

            print()

            ctlr = input('>> ')
            if ctlr.upper() == 'Q':
                break
            else:
                continue
