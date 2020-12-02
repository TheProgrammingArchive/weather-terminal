from bs4 import BeautifulSoup
import requests
import csv

class weatherHourly:
    def __init__(self, source):
        self.source = source
        self.src = requests.get(self.source).text
        self.soup = BeautifulSoup(self.src, features='lxml')

    def weather_atThisHour(self):
        weather_now = self.soup.find('div', class_='DaypartDetails--DetailSummaryContent--1c28m Disclosure--SummaryDefault--1z_mF')

        time_now = weather_now.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
        print(f'Time(Now): {time_now}')

        temperature_current = weather_now.find('div', class_='DetailsSummary--temperature--3FMlw').text
        print(f'Temperature(Now): {temperature_current}')

        weatherdesc_current = weather_now.find('div', class_='DetailsSummary--condition--mqdxh').text
        print(f'Weather Description(Now): {weatherdesc_current}')

        precipindex_current = weather_now.find('div', class_='DetailsSummary--precip--2ARnx').text
        print(f'Precipitation Index(Now): {precipindex_current}')

        windsdp_current = weather_now.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
        print(f'Wind Speed: {windsdp_current}')

    def getdateofreport(self):
        dateofreport = self.soup.find('h3', class_='HourlyForecast--longDate--3khKr').text
        print(dateofreport)

    def getHourlyweather(self):
        for reports in self.soup.find_all('details', class_='DaypartDetails--DayPartDetail--3yhtR Disclosure--themeList--uBa5q'):

            timeofreport = reports.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            print(f"Time: {timeofreport}")

            temperature_Now = reports.find('div', class_='DetailsSummary--temperature--3FMlw').text
            print(f"Temperature: {temperature_Now}")

            weather_description = reports.find('div', class_='DetailsSummary--condition--mqdxh').text
            print(f"Description: {weather_description}")

            precip_index = reports.find('div', class_='DetailsSummary--precip--2ARnx').text
            print(f"Precipitation Index: {precip_index}")

            wind_speed = reports.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            print(f"Wind speed: {wind_speed}")

            print()

            if(timeofreport >= '23:00'):
                break
            else:
                continue

# remove comments under this line to execute program
# rvx = weatherHourly('https://weather.com/en-IN/weather/hourbyhour/l/bfbafb71cea3672231349f36b198478ecc3d5fd524d0918b8051ee838f743675')
# rvx.getHourlyweather()
