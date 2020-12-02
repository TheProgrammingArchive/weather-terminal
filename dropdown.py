from bs4 import BeautifulSoup
import requests

def get_tendayweather(source):
    site_source = requests.get(source).text
    soup = BeautifulSoup(site_source, features='lxml')

    for dropdown_article in soup.find_all('div', class_='DaypartDetails--Content--XQooU DaypartDetails--contentGrid--3cYKg'):
    # print(dropdown_article)
        i = 0
        for date_time in dropdown_article.find_all('h3', class_='DailyContent--daypartName--3G5Y8'):
            date_time = date_time.text
            if(i == 0):
                print(date_time[0:7])
            else:
                break
            i = i + 1

        i = 0
        print()
        for temp_morning in dropdown_article.find_all('span', class_='DailyContent--temp--_8DL5'):
            temp_morning = temp_morning.text
            if(i == 0):
                print(f'Maximum Temperature: {temp_morning}')
            else:
                print(f'Minimum Temperature: {temp_morning}')
            i = i + 1

        i = 0
        print()
        for weather_desc in dropdown_article.find_all('p', class_='DailyContent--narrative--3AcXd'):
            weather_desc = weather_desc.text
            if(i == 0):
                print(f'Description (Currently): {weather_desc}')
            else:
                print(f'Description (Later): {weather_desc}')
            i = i + 1


        i = 0
        print()
        for details in dropdown_article.find_all('ul', class_='DetailsTable--DetailsTable--2qH8C DaypartDetails--DetailsTable--2fwt-'):
            for table_content in details.find_all('li', class_='DetailsTable--listItem--1MW7X'):
                table_content = table_content.text
                if(i == 0):
                    print(f'Humidity (Currently): {table_content[8:11]}')

                elif(i == 1):
                    print(f'UV Index (Currently): {table_content[8:20]}')

                elif(i == 2):
                    print(table_content)

                elif (i == 3):
                    print(table_content)

                elif (i == 4):
                    print(f'Humidity (Later): {table_content[8:20]}')

                elif(i == 5):
                    print(f'UV Index (Later): {table_content[8:20]}')

                elif(i == 6):
                    print(table_content)

                elif(i == 7):
                    print(table_content)
                i = i + 1

        print('\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# get_tendayweather('https://weather.com/en-IN/weather/tenday/l/bfbafb71cea3672231349f36b198478ecc3d5fd524d0918b8051ee838f743675')
