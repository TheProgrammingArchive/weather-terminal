import requests

r = requests.get("https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW?Goto=Redirected")
# the below line has been commented cuz its optional and mostly not needed.
# r2 = requests.get('https://weather.com/hr-HR/weather/today/l/TWXX0021:1:TW?Goto=Redirected')
# replace de-DE in the below link with appropriate locale(https://saimana.com/list-of-country-locale-code/) and get url
r3 = requests.get("https://weather.com/de-DE/")
print(r3.url)