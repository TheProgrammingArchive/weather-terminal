# weather.com-scraper

## DISCLAIMER:
  THE PROJECT IS CURRENTLY UNDER MAINTANENCE DUE TO A WEBSITE UPDATE FROM OUR SOURCE. PLEASE WAIT FOR A FEW DAYS TILL WE PATCH THE PROBLEM WITH STABLE RELEASE 1.3
  
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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
  
  __git clone https://github.com/TheProgrammingArchive/weather-terminal__, wait for it to get cloned!
  
  Now without exiting the directory, type "cd weather-terminal/weather-terminal" (_REMOVE QUOTES_), after doing so run: python application.py
  This should start the app!
  
## Command list:
  weather now: Displays the current weather<br/>
  weather today: Displays the weather for this day<br/>
  weather tenday: Displays weather for next ten days<br/>
  detailed tenday: Displays ten day weather with extended info<br/>
        
  weather -t: Displays current temperature<br/>
  weather -dew: Displays cloud dew point currently<br/>
  weather -prs: Displays precipitation percentage currently<br/>
  weather -par: Displays current atmospheric pressure (bar)<br/>
  weather -mnp: Displays moon phase<br/>
  weather -ws: Displays current wind speed and direction<br/>
  weather -hdu: Displays current humidity percentage <br/>
  weather -vis: Displays current visibility (km)<br/>
  weather -uv: Displays current UV index out of 10 (0 - Minimum, 10 - Maximum)<br/>
  weather -dsc: Displays current weather description<br/>
  weather -tab: Displays startup table again<br/>
  --h or -help: Displays help page<br/>
  --o or -options: Displays options(current) page<br/>
        
  clear(): clear screen<br/>
  loc -p: Change permanent location<br/>
  loc -t: Change temporary location<br/>
  loc -pr: Return to permanent location<br/>
  --loc: View if location is permanent or temporary<br/>
        
  settings: Turn toggle (for weather tenday and weather today) on or off<br/>
  exit: Exit application


