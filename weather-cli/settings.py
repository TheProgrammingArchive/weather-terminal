def settings_page():

    print('                         SETTINGS      ')
    print('\n------------------------------------------------------------------------------\n')

    while True:
        with open('settingspage.txt') as file:
            content = file.read()
            if content == '':
                fcc = open('settings_config.txt', 'w')
                fcc.write('ENABLED')
                fcc.close()

            print(f'TOGGLE: {content}')
            content_cpn = input('\nPress X to disable toggle, Y to enable toggle or Q to exit settings and save changes: ')
            if content_cpn.upper() == 'X':
                if content == 'ENABLED':
                    ftc = open('settingspage.txt', 'w')
                    ftc.seek(0)
                    ftc.truncate()
                    ftc.write('DISABLED')
                    ftc.close()
                    file.read()

                else:
                    print('Already disabled!')
                    continue

            elif content_cpn.upper() == 'Y':
                if content == 'DISABLED':
                    ftc = open('settingspage.txt', 'w')
                    ftc.seek(0)
                    ftc.truncate()
                    ftc.write('ENABLED')
                    ftc.close()
                    file.read()

                else:
                    print('ALREADY ENABLED')
                    continue

            elif content_cpn.upper() == 'Q':
                file.close()
                break

            elif content_cpn == '':
                continue
            else:
                continue

    return content

# rtn_vl = settings_page()
# # print(rtn_vl)
# settings_page()
