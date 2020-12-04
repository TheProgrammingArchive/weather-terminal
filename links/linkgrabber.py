import requests
from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser
import string

def get_Link():
    x = ""
    fulltext=""

    file = open('locations.txt', 'r')
    content = file.read()
    content = content.split('\n')
    print(content)

    country = input("Enter your country (If your country is the united states of america please enter it as united states of america/nameofyourstate):")

    country_conf = input('Please confirm your country: ')

    while(country_conf != country):
        country = input('Country confirmation did not match! Please enter your country again: ')
        country_conf = input('Confirm country: ')
        if(country == country_conf):
            break

    country_conf = string.capwords(country_conf)
    print(country_conf)

    while country_conf not in content:
        country = input('The country you have entered is not in our database! Please enter a valid country (Type COUNTRY in capitals to get the list of countries): ')
        if string.capwords(country) in content:
            print('Country found!')
            break
        elif country == 'COUNTRY':
            print(content)

    final_country = country.replace(" ", "-")
    final_country = final_country.lower()
    url = 'https://weather.codes/'+final_country+'/'
    print(url)
    reqs = requests.get(url)
    soupu = BeautifulSoup(reqs.text, 'lxml')
    inman = input("Enter your location: ")

    while len(inman) <= 2 or len(inman) >= 40:
        inman = input('Location string length too small! Please try again: ')

    #changes every first letter in input to capital
    capinman = string.capwords(inman)
    #find li tag and parses location from it
    for tag in soupu.find_all("li"):
        x = tag.text+"\n"
        if capinman in x:
           fulltext = fulltext+x + "\n"
           break

        elif capinman not in x:
            print('notf')


    listya = list(filter(bool, fulltext.splitlines()))
    lengthoflist = len(listya)

    i = 0

    for content in listya:
        print(f'{i+1}. {listya[i]}')
        i += 1

    print(i)

    #prints the locations
    # print(fulltext)
    #asks for location option

    while True:
        try:
            optionoflocation = int(input("Enter your option with the correspoding number to the location and code: "))
            while True:
                if optionoflocation > i or optionoflocation <= 0:
                    raise ValueError
                else:
                    break
        except ValueError:
            print('The value you have entered is invalid! Enter enter a valid integer.')
            continue
        else:
            break

    print(optionoflocation)

    #minuses one from option for list selecting
    listoption = int(optionoflocation)-1



    # print(lengthoflist)


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
        x = links5.get('href')
        #store so that can be accessed outside loop
        storageout=storageout+x

    storageout = storageout.split('/')
    code = storageout[4]
    return (code)

    file.close()

print(get_Link())