from weather_today import weatherHourly
from weather_tenday import weatherTenDay
from table import get_tableToday
import os
import time

class Application():

    def start_application(self):

        keywords = ['DBG', 'WEATHER TODAY', 'WEATHER TENDAY', 'DETAILED TENDAY', 'TIME -N', 'DATE -T', 'WEATHER -T', 'WEATHER -DSC', 'WEATHER -FLS', 'WEATHER -WS', 'WEATHER -HDU', 'WEATHER -DEW', 'WEATHER -PRS', 'WEATHER -UV', 'WEATHER -VIS', 'WEATHER -MNS', 'LOC -P', 'LOC -T', 'LOC -VIEW']
        file = open('gotloc.txt', 'r')

        location_content = file.read()
        location_content = location_content.split(':')

        file.close()
        print('Type -help or [--h] for help or -options or [--o] for commands!\n\n')

        while True:
            command_arg = input('> ')
            while command_arg == "":
                command_arg = input('> ')

            if command_arg.upper() in keywords:
                content_value = location_content[1]
                content_value = content_value.replace(' ', '')

                prefix_hrbr = f'https://weather.com/en-IN/weather/hourbyhour/l/{content_value}'
                prefix_tenday = f'https://weather.com/en-IN/weather/tenday/l/{content_value}'
                prefix_table = f'https://weather.com/en-IN/weather/today/l/{content_value}'

                weather_tdayf = weatherHourly(prefix_hrbr)
                weather_tendayf = weatherTenDay(prefix_tenday)
                weather_tendayfdet = weatherTenDay(prefix_tenday)
                weather_tble = get_tableToday(prefix_table)

                if command_arg.upper() == 'WEATHER TODAY':
                    weather_tdayf.getHourlyweather()
                if command_arg.upper() == 'WEATHER TENDAY':
                    weather_tendayf.weather_Details()

            else:
                print('Unknown command!\n ')
                continue

    def setup(self):
        print('Since this application is being run for the first time you will have to enter a few details before we get started!')
        print('Your default location for the app will be set now. Please wait for a second\n\n')

    def help_fs(self):
        time.sleep(3)
        print('Your location details have been setup successfully!\n\n')

    def help_startup(self):
        pass

if __name__ == '__main__':
    print('''
                                                                | | | |                        | (_)
                                             __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                             \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                              \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                               \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

    ''')

    if os.path.exists('gotloc.txt') == True:
        with open('gotloc.txt') as file:
            content = file.read()
            content= content.split(':')
            content = content[0]
            file.close()
        print(f'PLOC: {content}')

    if os.path.isfile('gotloc.txt'):
        with open('gotloc.txt') as f:
            ct = f.read()

            if len(ct) == 0:
                print('Unknown issue occured with file! Please launch the application again.')
                f.close()
                os.remove('gotloc.txt')

            else:
                newApplication = Application()
                newApplication.start_application()

    else:

        nsApplication = Application()
        nsApplication.setup()

        time.sleep(2)

        from linkgrabber import x
        nsApplication.help_fs()

        prefix = f'https://weather.com/en-IN/weather/hourbyhour/l/{x}'

        file = open('gotloc.txt', 'w')
        nslocation = weatherHourly(prefix)

        location_Get = nslocation.location_m()
        file.write(f'{location_Get}: {x}')

        file.close()

        nsApplication.help_startup()
        nsApplication.start_application()
else:
    raise ImportError
    exit(1)
