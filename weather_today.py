from bs4 import BeautifulSoup
import requests
import csv

global soup
global source

source = requests.get('https://weather.com/en-IN/weather/hourbyhour/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c').text
soup =  BeautifulSoup(source, features='lxml')

class weatherHourly:
    def weather_atThisHour(self):
        weather_now = soup.find('div', class_='DaypartDetails--DetailSummaryContent--1c28m Disclosure--SummaryDefault--1z_mF')

        time_now = weather_now.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
        return (f'Time(Current): {time_now}')

        temperature_current = weather_now.find('div', class_='DetailsSummary--temperature--3FMlw').text
        return (f'Temperature(Current): {temperature_current}')

        weatherdesc_current = weather_now.find('div', class_='DetailsSummary--condition--mqdxh').text
        return (f'Description(Current): {weatherdesc_current}')

        precipindex_current = weather_now.find('div', class_='DetailsSummary--precip--2ARnx').text
        return (f'Precip Index(Current): {precipindex_current}')
        windsdp_current = weather_now.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text


    def getdateofreport(self):
        dateofreport =  soup.find('h3', class_='HourlyForecast--longDate--3khKr').text
        return (f'Date of report: {dateofreport}')

    def getHourlyweather(self):
        for reports in soup.find_all('details', class_='DaypartDetails--DayPartDetail--3yhtR Disclosure--themeList--uBa5q'):
            # return(report)
            timeofreport = reports.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            return(f'Time: {timeofreport}')

            temperature_Now = reports.find('div', class_='DetailsSummary--temperature--3FMlw').text
            return (f'Temperature: {temperature_Now}')

            weather_description = reports.find('div', class_='DetailsSummary--condition--mqdxh').text
            return (f'Description: {weather_description}')

            precip_index = reports.find('div', class_='DetailsSummary--precip--2ARnx').text
            return (f'Precip Index: {precip_index}')

            wind_speed = reports.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            return (f'Wind Speed: {wind_speed}')

            if(timeofreport == '23:30'):
                break
            else:
                continue

                

