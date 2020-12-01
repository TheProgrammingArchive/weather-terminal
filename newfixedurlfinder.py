import requests
from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser
import string
#todo: implement to check if country is valid or not, check if option entered is valid or not
x = ""
fulltext=""
country = input("enter your country:")
final_country = country.replace(" ", "-")
url = 'https://weather.codes/'+final_country+'/'
reqs = requests.get(url)
soupu = BeautifulSoup(reqs.text, 'lxml')
inman = input("Enter your location: ")
#changes every first letter in input to capital
capinman = string.capwords(inman)
#find li tag and parses location from it
for tag in soupu.find_all("li"):
    x = tag.text+"\n"
    if capinman in x:
       fulltext = fulltext+x + "\n"
#stores to list so can be accessed with option of user
listya = list(filter(bool, fulltext.splitlines()))
#gets length of list for "if condition" so we can check if option valid or not which i didnt know how to implement
lengthoflist = len(listya)
#prints the locations
print(fulltext)
#asks for location option
optionoflocation = input("Enter your option: ")
#minuses one from option for list selecting
listoption = int(optionoflocation)-1
optiontest = str(listya[listoption])
code = optiontest[-8:]
storageout=""

#gets page with weathercode obtained
source = requests.get('https://weather.com/weather/today/l/'+code).text

soup = BeautifulSoup(source, 'lxml')
#parses using bs4
links = soup.find('a', class_='ListItem--listItem--1r7mf styles--listItem--2JY_Z Button--default--2yeqQ')
links5 = str(links)
soup = BeautifulSoup(links5, "html.parser")
for links5 in soup.findAll('a'):
    x = 'https://weather.com'+links5.get('href')
    #store so that can be accessed outside loop
    storageout=storageout+x
#finally prints url
print(storageout)
