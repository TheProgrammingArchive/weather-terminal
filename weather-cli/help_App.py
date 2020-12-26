def help_application():
    print(
        '''
        Please make sure to read this file before proceeding to use the app, this module will go through all the command usages and usage of the app.
        NOTE: FOR LATER USAGE, IF YOU ONLY WANT TO VIEW THE LIST OF COMMANDS TYPE --O OR -OPTIONS. TYPE -HELP OR --H ONLY WHEN NEEDING ASSISTANCE IN USING THE APP.
    
        Startup:
            When you first start up the app, it will ask you for your country and location. This is stored permanently and can be changed in the future.
            This system helps to reduce time when logging in to check the current weather
        '''
    )
    _ = input('Press enter to read more >> ')

    print(
        '''
        Command line modifications:
            When in the MAIN command line you will see a > which denotes an input suggestion. Here you can enter any command from the list below!
            When in sections like weather ten day or weather today, you will see a >> which means you are in the terminal for that particular weather section.
            The toggle feature can change the way the input method works
        '''
    )

    _ = input('Press enter to read more >> ')

    print(
        '''
        Settings:
            This app currently has a toggle feature, as explained in the Command line modifications section above.
            Toggle helps to change the way the day/hour navigation system works under the weather ten day and weather today sections.
            If you have settings toggle enabled you can navigate using the letter P(Previous hr/day), N(Next hr/day), E(Extended info), Q(exit to main cli).
            If you have settings disabled then you can navigate using Enter(next day) or Q(exit to main cli).
        '''
    )

    _ = input('Press enter to read more >> ')

    print(
        '''
        Location change:
            There are primarily 2 location change commands in this app. loc -p and loc -t
            Loc -p changes your permanent location, this changes every section in the app from the startup dropdown display and the weather sections
            Loc -t changes your location temporarily, this is useful when you want to view the weather of another location temporarily
            To know if you're in a temporary location or not just scroll up and you'll see your location somewhere near the title
            If there is a text which says 'Temporary Location', it means you're currently not in the permanent selected location, an alternate way to check is by typing the command --loc, 
            this will tell you if you have permanent location selected or not
            
            To change back to permanent selected location type the command loc -pr and you'll be taken back.
        '''
    )

    _ = input('Press enter to read more >> ')

    print(
        '''
        Title screen weather:
            When you load up the app, you will usually see a dropdown box which displays the hourly weather. This box is dynamic and the amount of information changes according to the size of your terminal.
            It is recommended to have your terminal set to the default size!
        '''
    )

    _ = input('Press enter to read more >> ')

    print(
        '''
        Other information:
            Under the weather hourly section, if toggle is enabled and if it's the last hour of the day. The section will display only the particular weather for the next hour and exit the section
            this is because weather.com uses a separate tag for the current weather, you can view it only by typing the command weather now.
            
            
        Exiting the app:
            Please try to use only the EXIT command to exit the app, you can use CTRL-Z ent or CTRL-C to exit but these exit methods create issues when in the loc -p section.
            If CTRL-C or CTRL-Z in pressed in the loc -p section, it leads to a corrupt file issue sometimes. The next time you open the app an error will be displayed on the screen.
        '''
    )

    _ = input('Press enter to read more >> ')

    print(
        '''
        Errors:
            1. Port connection: 
                If you try to use the app without access to the internet or have a very slow connection, you'll get a port connection error
                Make sure you're connected to the internet or just wait for sometime and the issue will get resolved
                
            2. File error:
                If as mentioned in the above section (exiting the app), CTRL-Z ent or CTRL-C can produce errors when used in the loc -p section.
                When this occurs the app will close automatically and the next time you open it, the app will be reset meaning that you'd have to enter your permanent location again.
                Other than that there's no major issue using CTRL-Z ent or CTRL-C
                
            3. Requests error:
                This error can only occur if you modify the contents of any of the location files.
                If this occurs, make sure to delete the gotloc.txt file when launching the application again.
    
        '''
    )
    
    _ = input('Press enter to exit help >> ')

def options_displ():
    print(
        '''
        weather now: Displays the current weather
        weather today: Displays the weather for this day
        weather tenday: Displays weather for next ten days
        detailed tenday: Displays ten day weather with extended info
        
        weather -t: Displays current temperature
        weather -dew: Displays cloud dew point currently
        weather -prs: Displays precipitation percentage currently
        weather -par: Displays current atmospheric pressure (bar)
        weather -mnp: Displays moon phase
        weather -ws: Displays current wind speed and direction
        weather -hdu: Displays current humidity percentage 
        weather -vis: Displays current visibility (km)
        weather -uv: Displays current UV index out of 10 (0 - Minimum, 10 - Maximum)
        weather -dsc: Displays current weather description
        weather -tab: Displays startup table again
        
        --h or -help: Displays help page
        --o or -options: Displays options(current) page
        
        clear(): clear screen
        loc -p: Change permanent location
        loc -t: Change temporary location
        loc -pr: Return to permanent location
        --loc: View if location is permanent or temporary
        
        settings: Turn toggle on or off
        exit: Exit application
        
        '''
    )
