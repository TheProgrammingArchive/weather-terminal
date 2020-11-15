from bs4 import BeautifulSoup
import requests

site_source = requests.get('https://weather.com/en-IN/weather/tenday/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c').text
soup = BeautifulSoup(site_source, features='lxml')

dropdown_article = soup.find('div', class_='DaypartDetails--Content--XQooU DaypartDetails--contentGrid--3cYKg')
# print(dropdown_article)
for date_time in dropdown_article.find_all('h3', class_='DailyContent--daypartName--3G5Y8'):
    print(date_time.text)

for temp_morning in dropdown_article.find_all('span', class_='DailyContent--temp--_8DL5'):
    print(temp_morning.text)
    
