from weather_today import weatherHourly
from dropdown import get_tendayweather
from weather_tenday import weatherTenDay
from table import get_tableToday
from toggle_module import toggle_tenday, toggle_drpdw
import settings
import importlib
import os
import time
import webbrowser

def title():
    print('''
                                                                    | | | |                        | (_)
                                                 __      _____  __ _| |_| |__   ___ _ __ ______ ___| |_ 
                                                 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______/ __| | |
                                                  \ V  V /  __/ (_| | |_| | | |  __/ |        | (__| | |
                                                   \_/\_/ \___|\__,_|\__|_| |_|\___|_|         \___|_|_|

        ''')

class Application():

    def start_application(self):

        keywords = ['SETTINGS', 'CLEAR()','EXIT','WEATHER TODAY', 'WEATHER NOW', 'WEATHER TENDAY', 'DETAILED TENDAY', 'TIME -N', 'DATE -T', 'WEATHER -T', 'WEATHER -DSC', 'WEATHER -PRS', 'WEATHER -WS', 'WEATHER -HDU', 'WEATHER -DEW', 'WEATHER -PAR','WEATHER -UV', 'WEATHER -VIS', 'WEATHER -MNP', 'LOC -P', 'LOC -T', 'LOC -FAV']

        print('Type -help or [--h] for help or -options or [--o] for commands!\n\n')

        while True:
            print()
            command_arg = input('> ')
            while command_arg == "":
                command_arg = input('> ')

            if command_arg.upper() in keywords:
                file = open('gotloc.txt', 'r')

                location_content = file.read()
                location_content = location_content.split(':')
                # print(location_content)

                file.close()

                content_value = location_content[1]
                content_value = content_value.replace(' ', '')

                prefix_hrbr = f'https://weather.com/en-IN/weather/hourbyhour/l/{content_value}'
                prefix_tenday = f'https://weather.com/en-IN/weather/tenday/l/{content_value}'
                prefix_table = f'https://weather.com/en-IN/weather/today/l/{content_value}'

                weather_tdayf = weatherHourly(prefix_hrbr)
                weather_tendayf = weatherTenDay(prefix_tenday)

                weather_tble = get_tableToday(prefix_table)
                toggle_wtenday = toggle_tenday.weatherTenDay_toggle(prefix_tenday)

                if command_arg.upper() == 'SETTINGS':
                    settings_content = settings.settings_page()
                    print(f'Toggle is now: {settings_content}')

                elif command_arg.upper() == 'TIME -N':
                    weather_tendayf.timeof_report()

                elif command_arg.upper() == 'DATE -T':
                    weather_tdayf.getdateofreport()

                elif command_arg.upper() == 'WEATHER -T':
                    trpt = weather_tdayf.current_temperature()
                    print(f'{trpt}')

                elif command_arg.upper() == 'WEATHER -DSC':
                    trpt = weather_tdayf.weather_desc()
                    print(f'{trpt}')

                elif command_arg.upper() == 'WEATHER -PRS':
                    trpt = weather_tdayf.precip_current()
                    print(f'{trpt}')

                elif command_arg.upper() == 'WEATHER -WS':
                    trpt = weather_tdayf.wspeed()
                    print(f'{trpt}')

                elif command_arg.upper() == 'WEATHER TODAY':
                    weather_tdayf.getHourlyweather()

                elif command_arg.upper() == 'WEATHER NOW':
                    weather_tdayf.weather_atThisHour()

                elif command_arg.upper() == 'WEATHER TENDAY':
                    with open('settingspage.txt') as settings_file:
                        context = settings_file.read()
                        if context == 'ENABLED':
                            toggle_wtenday.weather_Details()

                        elif context == 'DISABLED':
                            weather_tendayf.weather_Details()

                elif command_arg.upper() == 'WEATHER -HDU':
                    hdu = weather_tble[2]
                    hdu = hdu[8:]
                    print(f'Humidity: {hdu}')

                elif command_arg.upper() == 'WEATHER -DEW':
                    dew = weather_tble[3]
                    dew = dew[9: ]
                    print(f'Dew point: {dew}')

                elif command_arg.upper() == 'WEATHER -PAR':
                    prs = weather_tble[4]
                    prs = prs[8: ]
                    print(f'Atm pressure: {prs}')

                elif command_arg.upper() == 'WEATHER -UV':
                    uv = weather_tble[5]
                    uv = uv[8: ]
                    print(f'UV Index: {uv}')

                elif command_arg.upper() == 'WEATHER -VIS':
                    vis = weather_tble[6]
                    vis = vis[10: ]
                    print(f'Visibility: {vis}')

                elif command_arg.upper() == 'WEATHER -MNP':
                    mnp = weather_tble[7]
                    mnp = mnp[10: ]
                    print(f'Moon phase: {mnp}')

                elif command_arg.upper() == 'CLEAR()':
                    toggle_tenday.clear()
                    title()
                    print(f'Location: {location_content[0]}')

                elif command_arg.upper() == 'LOC -P':
                    confirmation = input('\n\nAre you sure you want to change your permanent location (Y/N)? >> ')

                    if confirmation.upper() == 'Y':
                        with open('gotloc.txt', 'w') as filenew:
                            filenew.seek(0)
                            filenew.write('')

                            from linkgrabber import x

                            prefix = f'https://weather.com/en-IN/weather/hourbyhour/l/{x}'
                            nslocation = weatherHourly(prefix)

                            location_Get = nslocation.location_m()
                            filenew.write(f'{location_Get}: {x}')

                            filenew.seek(0)
                            filenew.close()

                    elif confirmation.upper() == 'N':
                        print('Exiting location change')
                        continue

                    else:
                        continue

                elif command_arg.upper() == 'DETAILED TENDAY':
                    with open('settingspage.txt') as fr:
                        contel = fr.read()
                        if contel == 'ENABLED':
                            toggle_wtenday.weather_Details()

                        elif contel == 'DISABLED':
                            weather_tendayfdtl = get_tendayweather(prefix_tenday)

                elif command_arg.upper() == '':
                    pass

                elif command_arg.upper() == 'EXIT':
                    time.sleep(3)
                    exit()

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
    title()

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
        f.close()

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
