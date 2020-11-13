from bs4 import BeautifulSoup
import requests
import csv

global soup
global source
source1 = requests.get('https://weather.com/en-SG/weather/today/l/SNXX0006:1:SN?Goto=Redirected').text

soup1 = BeautifulSoup(source1, 'lxml')
links = soup1.find('a', class_='ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ')
links5 = str(links)
links1 =links5.replace('<a class="ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ" data-from-string="localsuiteNav_2_Hourly" href="', "")
link3 = links1.replace('" target="_self"><span class="styles--liContent--1nCd7">Hourly</span></a>', "")
finallink= "https://weather.com"+link3
source = requests.get(finallink).text
soup =  BeautifulSoup(source, features='lxml')

class weatherHourly:
    def weather_atThisHour(self):
        weather_now = soup.find('div', class_='DaypartDetails--DetailSummaryContent--1c28m Disclosure--SummaryDefault--1z_mF')

        time_now = weather_now.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
        print(f'Time(Current): {time_now}')

        temperature_current = weather_now.find('div', class_='DetailsSummary--temperature--3FMlw').text
        print(f'Temperature(Current): {temperature_current}')

        weatherdesc_current = weather_now.find('div', class_='DetailsSummary--condition--mqdxh').text
        print(f'Description(Current): {weatherdesc_current}')

        precipindex_current = weather_now.find('div', class_='DetailsSummary--precip--2ARnx').text
        print(f'Precip Index(Current): {precipindex_current}')
        windsdp_current = weather_now.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text


    def getdateofreport(self):
        dateofreport =  soup.find('h3', class_='HourlyForecast--longDate--3khKr').text
        print(f'Date of report: {dateofreport}')

    def getHourlyweather(self):
        for reports in soup.find_all('details', class_='DaypartDetails--DayPartDetail--3yhtR Disclosure--themeList--uBa5q'):
            # print(report)
            print('\n')
            timeofreport = reports.find('h2', class_='DetailsSummary--daypartName--1Mebr').text
            print(f'Time: {timeofreport}')

            temperature_Now = reports.find('div', class_='DetailsSummary--temperature--3FMlw').text
            print(f'Temperature: {temperature_Now}')

            weather_description = reports.find('div', class_='DetailsSummary--condition--mqdxh').text
            print(f'Description: {weather_description}')

            precip_index = reports.find('div', class_='DetailsSummary--precip--2ARnx').text
            print(f'Precip Index: {precip_index}')

            wind_speed = reports.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text
            print(f'Wind Speed: {wind_speed}')

            if(timeofreport == '23:30'):
                break
            else:
                continue
weatherHourly.getdateofreport(None)