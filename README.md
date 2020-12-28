# weather.com-scraper

## About the project:
  Get daily weather from your cli!
  
## Requirements:
  For this application to work make sure you have python 3.7 or greater added to path. Make sure you have done so by opening cmd and typing 'pip --version' without quotes. If you get the version info then it means it has been added to your path successfully! If not please refer on how to add py to path. 
  
  Pkgs to install: requests, lxml, bs4, art, tableprint. (For more info please view requirements.txt file)
  Command: pip install {pkgname}
  
## CLONING AND RUNNING THE APP:
  To clone the project follow the steps:
  Navigate to the directory where you want to clone the project by using 'cd directoryname' (_REMOVE QUOTES_). Once you are in the directory where you want to clone it, run the 
  following command:
  
  __git clone https://github.com/TheProgrammingArchive/weather.com-scraper__, wait for it to get cloned!
  
  Now without exiting the directory, type "cd weather.com-scraper/weather-cli" (_REMOVE QUOTES_), after doing so run: python application.py
  This should start the app!
  
## Command list:
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
  
## INSTALLING FROM PYPI:
  Run pip install weather-terminal.


