from weather_today import weatherHourly
import weather_tenday_toggle
from weather_tenday_toggle import weatherTenDay_toggle
from table import get_tableToday
from toggle_module import toggle_tenday_ext, toggle_drpdw, weather_today_toggle
from weather_Tenday import weatherTenDay
from weathertodayaio import weatherHoury
import settings
import help_App
import importlib
import os
import time
import webbrowser
import string
import shutil


def title():
    title_content = '''
                     _   _                      _                      _             _ 
                    | | | |                    | |                    (_)           | |
 __      _____  __ _| |_| |__   ___ _ __ ______| |_ ___ _ __ _ __ ___  _ _ __   __ _| |
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|______| __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
  \ V  V /  __/ (_| | |_| | | |  __/ |         | ||  __/ |  | | | | | | | | | | (_| | |
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|          \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                                                                                                                                                                                            
                    '''
    for shutter_title in title_content.split('\n'):
        print(shutter_title.center(shutil.get_terminal_size().columns))


class Application:
    @staticmethod
    def help_app():
        weather_tenday_toggle.clear()
        title()
        print('\n')
        entr = input('Press enter for help or Q to exit help: ')
        if entr == 'Q':
            with open('gotloc.txt') as file_erb:
                content_erb = file_erb.read()
                content_erb = content_erb.split(':')
                content_erb = content_erb[1]
                ui_src_erb = f'https://weather.com/en-IN/weather/hourbyhour/l/{content_erb}'
                uiprs_erb = weatherHoury(ui_src_erb)
                uiprs_erb.weather_atThisHour()
                file.close()

        elif entr == '':
            weather_tenday_toggle.clear()
            title()
            help_App.help_application()
            weather_tenday_toggle.clear()
            title()

            with open('gotloc.txt') as file_erb:
                content_erb = file_erb.read()
                content_erb = content_erb.split(':')
                content_erb = content_erb[1]
                ui_src_erb = f'https://weather.com/en-IN/weather/hourbyhour/l/{content_erb}'
                uiprs_erb = weatherHoury(ui_src_erb)
                uiprs_erb.weather_atThisHour()
                file.close()


            print('\nType -help or [--h] for help and -options or [--o] for options and EXIT to exit!\n\n')

        else:
            with open('gotloc.txt') as file_erb:
                content_erb = file_erb.read()
                content_erb = content_erb.split(':')
                content_erb = content_erb[1]
                ui_src_erb = f'https://weather.com/en-IN/weather/hourbyhour/l/{content_erb}'
                uiprs_erb = weatherHoury(ui_src_erb)
                uiprs_erb.weather_atThisHour()
                file.close()

    @staticmethod
    def start_application():

        keywords = ['--H', '-HELP', 'SETTINGS', 'CLEAR()', 'EXIT', 'WEATHER TODAY', 'WEATHER NOW', 'WEATHER TENDAY',
                    'DETAILED TENDAY', 'DATE -T', 'WEATHER -T', 'WEATHER -DSC', 'WEATHER -PRS',
                    'WEATHER -WS', 'WEATHER -HDU', 'WEATHER -DEW', 'WEATHER -PAR', 'WEATHER -UV', 'WEATHER -VIS',
                    'WEATHER -MNP', 'LOC -P', 'LOC -T', 'LOC -PR', '--LICENSE', '--CONTRIBUTORS', '--CREDITS', '--REQS', '--LOC', '--O', '-OPTIONS', 'WEATHER -TAB']

        print('\nType -help or [--h] for help and -options or [--o] for options and EXIT to exit!\n\n')

        while True:
            print()
            command_arg = input('> ')
            while command_arg == "":
                command_arg = input('> ')

            if command_arg.upper() in keywords:

                if os.path.isfile('temploc.txt') == True:
                    filo = open('temploc.txt', 'r')
                    location_content = filo.read()
                    location_content = location_content.split(':')
                    filo.close()

                else:
                    file = open('gotloc.txt', 'r')
                    location_content = file.read()
                    location_content = location_content.split(':')
                    file.close()

                # print(location_content)

                content_value = location_content[1]
                content_value = content_value.replace(' ', '')

                prefix_hrbr = f'https://weather.com/en-IN/weather/hourbyhour/l/{content_value}'
                prefix_tenday = f'https://weather.com/en-IN/weather/tenday/l/{content_value}'
                prefix_table = f'https://weather.com/en-IN/weather/today/l/{content_value}'

                weather_tdayf = weatherHourly(prefix_hrbr)
                weather_tdayfd = weather_today_toggle.WeatherToggleHourly(prefix_hrbr)
                weather_tendayf = weatherTenDay_toggle(prefix_tenday)

                weather_tble = get_tableToday(prefix_table)
                toggle_wtenday = weatherTenDay_toggle(prefix_tenday)
                toggle_dtenday = toggle_tenday_ext.weatherTenDay_toggle_dble(prefix_tenday)
                weathertenday = weatherTenDay(prefix_tenday)

                if command_arg.upper() == 'SETTINGS':
                    settings_content = settings.settings_page()
                    print(f'Toggle is now: {settings_content}')

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

                elif command_arg.upper() == 'WEATHER -TAB':
                    if os.path.isfile('temploc.txt'):
                        weather_tenday_toggle.clear()

                        title()

                        with open('temploc.txt') as file:
                            conr = file.read()
                            conr = conr.split(':')
                            conr = conr[1]
                            conr = conr.replace(' ', '')

                            src = f'https://www.weather.com/en-IN/weather/hourbyhour/l/{conr}'
                            ubiq = weatherHoury(src)
                            ubiq.weather_atThisHour()
                            file.close()
                            print(
                                '\nType -help or [--h] for help and -options or [--o] for options and EXIT to exit!\n\n')

                    elif not os.path.isfile('temploc.txt'):
                        weather_tenday_toggle.clear()

                        title()

                        with open('gotloc.txt') as file:
                            conr = file.read()
                            conr = conr.split(':')
                            conr = conr[1]
                            conr = conr.replace(' ', '')

                            src = f'https://www.weather.com/en-IN/weather/hourbyhour/l/{conr}'
                            ubiq = weatherHoury(src)
                            ubiq.weather_atThisHour()
                            file.close()
                            print(
                                '\nType -help or [--h] for help and -options or [--o] for options and EXIT to exit!\n\n')

                elif command_arg.upper() == '-OPTIONS' or command_arg.upper() =='--O':
                    help_App.options_displ()

                elif command_arg.upper() == "LOC -PR":
                    if os.path.isfile('temploc.txt'):
                        os.remove('temploc.txt')
                        print('Returning to permanent location!')
                        weather_tenday_toggle.clear()

                        title()

                        with open('gotloc.txt') as file:
                            conr = file.read()
                            conr = conr.split(':')
                            conr = conr[1]
                            conr = conr.replace(' ', '')

                            src = f'https://www.weather.com/en-IN/weather/hourbyhour/l/{conr}'
                            ubiq = weatherHoury(src)
                            ubiq.weather_atThisHour()

                    else:
                        print('Temporary location not selected!')
                        continue

                elif command_arg.upper() == 'WEATHER -WS':
                    trpt = weather_tdayf.wspeed()
                    print(f'{trpt}')

                elif command_arg.upper() == '--LOC':
                    if os.path.isfile('temploc.txt'):
                        with open('temploc.txt') as fln:
                            frl = fln.read()
                            frl = frl.split(':')
                            frl = frl[0]
                            print(f'Temporary location: {frl}')

                    elif not os.path.isfile('temploc.txt'):
                        if os.path.isfile('gotloc.txt'):
                            with open('gotloc.txt') as fln:
                                frl = fln.read()
                                frl = frl.split(':')
                                frl = frl[0]
                                print(f'Permanent Location: {frl}')

                elif command_arg.upper() == 'WEATHER TODAY':
                    with open('settingspage.txt') as file_hrbr:
                        content_xrbr = file_hrbr.read()
                        if content_xrbr == 'ENABLED':
                            weather_tdayfd.get_togglehrhr()

                        elif content_xrbr == 'DISABLED':
                            weather_tdayf.getHourlyweather()

                elif command_arg.upper() == 'WEATHER NOW':
                    weather_tdayf.weather_atThisHour()

                elif command_arg.upper() == 'WEATHER TENDAY':
                    with open('settingspage.txt') as settings_file:
                        context = settings_file.read()
                        if context == 'ENABLED':
                            toggle_wtenday.weather_Details()

                        elif context == 'DISABLED':
                            weathertenday.weather_Details()

                elif command_arg.upper() == 'WEATHER -HDU':
                    hdu = weather_tble[2]
                    hdu = hdu[8:]
                    print(f'Humidity: {hdu}')

                elif command_arg.upper() == 'WEATHER -DEW':
                    dew = weather_tble[3]
                    dew = dew[9:]
                    print(f'Dew point: {dew}')

                elif command_arg.upper() == 'WEATHER -PAR':
                    prs = weather_tble[4]
                    prs = prs[8:]
                    print(f'Atm pressure: {prs}')

                elif command_arg.upper() == 'WEATHER -UV':
                    uv = weather_tble[5]
                    uv = uv[8:]
                    print(f'UV Index: {uv}')

                elif command_arg.upper() == 'WEATHER -VIS':
                    vis = weather_tble[6]
                    vis = vis[10:]
                    print(f'Visibility: {vis}')

                elif command_arg.upper() == 'WEATHER -MNP':
                    mnp = weather_tble[7]
                    mnp = mnp[10:]
                    print(f'Moon phase: {mnp}')

                elif command_arg.upper() == 'CLEAR()':
                    weather_tenday_toggle.clear()
                    title()
                    if os.path.isfile('temploc.txt'):
                        print(f'Temporary location: {location_content[0]}')

                    else:
                        print(f'Location: {location_content[0]}')
                    print('\nType -help or [--h] for help and -options or [--o] for options and EXIT to exit!\n\n')

                elif command_arg.upper() == 'LOC -T':
                    fltemp = open('temploc.txt', 'w+')
                    fltemp.seek(0)
                    fltemp.write('')

                    from linkgrabber import get_Link

                    x = get_Link()

                    prefix = f'https://weather.com/en-IN/weather/hourbyhour/l/{x}'
                    nslocation = weatherHourly(prefix)

                    location_Get = nslocation.location_m()
                    fltemp.write(f'{location_Get}: {x}')

                    fltemp.seek(0)
                    fltemp.close()

                    weather_tenday_toggle.clear()
                    title()

                    with open('temploc.txt') as file:
                        conr = file.read()
                        conr = conr.split(':')
                        conr = conr[1]
                        conr = conr.replace(' ', '')

                        src = f'https://www.weather.com/en-IN/weather/hourbyhour/l/{conr}'
                        ubiq = weatherHoury(src)
                        loc_view = 'Temporary Location'
                        print(loc_view.center(shutil.get_terminal_size().columns))
                        ubiq.weather_atThisHour()

                elif command_arg.upper() == 'LOC -P':
                    confirmation = input('\n\nAre you sure you want to change your permanent location (Y/N)? >> ')

                    if confirmation.upper() == 'Y':
                        with open('gotloc.txt', 'w') as filenew:
                            filenew.seek(0)
                            filenew.write('')

                            from linkgrabber import get_Link
                            x = get_Link()

                            prefix = f'https://weather.com/en-IN/weather/hourbyhour/l/{x}'
                            nslocation = weatherHourly(prefix)

                            location_Get = nslocation.location_m()
                            filenew.write(f'{location_Get}: {x}')

                            filenew.seek(0)
                            filenew.close()

                            weather_tenday_toggle.clear()
                            title()

                            with open('gotloc.txt') as file:
                                conr = file.read()
                                conr = conr.split(':')
                                conr = conr[1]
                                conr = conr.replace(' ', '')

                                src = f'https://www.weather.com/en-IN/weather/hourbyhour/l/{conr}'
                                ubiq = weatherHoury(src)
                                ubiq.weather_atThisHour()

                    elif confirmation.upper() == 'N':
                        print('Exiting location change')
                        continue

                    else:
                        continue

                elif command_arg.upper() == 'DETAILED TENDAY':
                    toggle_dtenday.weather_Details()

                elif command_arg.upper() == '-HELP' or command_arg.upper() == '--H':
                    Application.help_app()

                elif command_arg.upper() == '':
                    pass

                elif command_arg.upper() == 'EXIT':
                    if os.path.isfile('temploc.txt'):
                        os.remove('temploc.txt')

                    time.sleep(1.5)
                    exit()

            else:
                print('Unknown command!\n ')
                continue

    def setup(self):
        print(
            'Since this application is being run for the first time you will have to enter a few details before we get started!')
        print('Your default location for the app will be set now. Please wait for a second\n\n')

    def help_fs(self):
        time.sleep(3)
        print('Your location details have been setup successfully!\n\n')


if __name__ == '__main__':
    title()

    if os.path.isfile('temploc.txt') == True:
        os.remove('temploc.txt')

    else:
        pass

    # if os.path.exists('gotloc.txt') == True:

    #     with open('gotloc.txt') as file:
    #         content = file.read()
    #         content = content.split(':')
    #         content = content[0]
    #         file.close()
    #     print(f'Location: {content}')

    if os.path.isfile('gotloc.txt'):
        with open('gotloc.txt') as f:
            ct = f.read()

            if len(ct) == 0:
                print('Unknown issue occured with file! Please launch the application again.')
                f.close()
                os.remove('gotloc.txt')

            else:
                with open('gotloc.txt') as file:
                    content = file.read()
                    content = content.split(':')
                    content = content[1]
                    ui_src = f'https://weather.com/en-IN/weather/hourbyhour/l/{content}'
                    uiprs = weatherHoury(ui_src)
                    uiprs.weather_atThisHour()
                file.close()

                newApplication = Application()
                newApplication.start_application()
        f.close()

    else:

        nsApplication = Application()
        nsApplication.setup()

        time.sleep(2)

        from linkgrabber import get_Link

        x = get_Link()
        nsApplication.help_fs()

        prefix = f'https://weather.com/en-IN/weather/hourbyhour/l/{x}'

        file = open('gotloc.txt', 'w')
        nslocation = weatherHourly(prefix)

        location_Get = nslocation.location_m()
        file.write(f'{location_Get}: {x}')

        file.close()

        with open('gotloc.txt') as file:
            content = file.read()
            content = content.split(':')
            content = content[1]
            ui_src = f'https://weather.com/en-IN/weather/hourbyhour/l/{content}'
            uiprs = weatherHoury(ui_src)
            uiprs.weather_atThisHour()
            file.close()

        nsApplication.start_application()
else:
    raise (
        ImportError
    )