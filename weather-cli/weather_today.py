from bs4 import BeautifulSoup
import requests
import csv

class weatherHourly:
    def __init__(self, source):
        self.source = source
        self.src = requests.get(self.source).text
        self.soup = BeautifulSoup(self.src, features='lxml')
        self.weather_now = self.soup.find('div', class_='DaypartDetails--DetailSummaryContent--1c28m Disclosure--SummaryDefault--1z_mF')

    def location_m(self):
        location = self.soup.find('span', class_='LocationPageTitle--PresentationName--Injxu')
        location = location.text
        return location
        # print(location)

    def weather_atThisHour(self):
        time_now = self.weather_now.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
        print(f'Update as of: {time_now}')

        temperature_current = self.weather_now.find('div', class_='DetailsSummary--temperature--3FMlw').text
        print(f'Temperature(Now): {temperature_current}')

        weatherdesc_current = self.weather_now.find('div', class_='DetailsSummary--condition--mqdxh').text
        print(f'Weather Description(Now): {weatherdesc_current}')

        precipindex_current = self.weather_now.find('div', class_='DetailsSummary--precip--2ARnx').text
        print(f'Precipitation Index(Now): {precipindex_current}')

        windsdp_current = self.weather_now.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
        print(f'Wind Speed: {windsdp_current}')

    def getdateofreport(self):
        dateofreport = self.soup.find('h3', class_='HourlyForecast--longDate--3khKr').text
        print(dateofreport)

    def getHourlyweather(self):
        for reports in self.soup.find_all('details', class_='DaypartDetails--DayPartDetail--3yhtR Disclosure--themeList--uBa5q'):

            timeofreport = reports.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            print(f"Updated at: {timeofreport}")

            temperature_Now = reports.find('div', class_='DetailsSummary--temperature--3FMlw').text
            print(f"Temperature: {temperature_Now}")

            weather_description = reports.find('div', class_='DetailsSummary--condition--mqdxh').text
            print(f"Description: {weather_description}")

            precip_index = reports.find('div', class_='DetailsSummary--precip--2ARnx').text
            print(f"Precipitation Index: {precip_index}")

            wind_speed = reports.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            print(f"Wind speed: {wind_speed}")

            print('\n\n----------------------------------------------------------------------------------------\n')

            if(timeofreport >= '23:00'):
                break
            else:
                continue

    def current_temperature(self):
        temperature_crr = self.weather_now.find('div', class_='DetailsSummary--temperature--3FMlw').text
        return (f'Temperature(Now): {temperature_crr}')

    def weather_desc(self):
        weatherdesc_crr = self.weather_now.find('div', class_='DetailsSummary--condition--mqdxh').text
        return (f'Weather Description(Now): {weatherdesc_crr}')

    def precip_current(self):
        precipindex_crr = self.weather_now.find('div', class_='DetailsSummary--precip--2ARnx').text
        return (f'Precipitation Index(Now): {precipindex_crr}')

    def wspeed(self):
        windsdp_current = self.weather_now.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
        return (f'Wind Speed: {windsdp_current}')

# rvx = weatherHourly('https://weather.com/en-IN/weather/hourbyhour/l/7f4609db5007684b5c20c12f0d71f3d95d207282ec1d8361f10670468549c54f')
# # rvx.getHourlyweather()
# rvx.weather_atThisHour()
