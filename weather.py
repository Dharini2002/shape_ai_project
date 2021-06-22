import requests
import os,socket
from datetime import datetime

os.system('cls')
api_key = '8c7a4c2ab386bff4887b5a7c7a9b0155'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
file = open('output.txt','w')
file.write ('*' * 40)
file.write('\n')
file.write ("Weather Status for - {}  || {}".format(location.upper(), date_time))
file.write('\n')
file.write ('*' * 40)
file.write('\n')
file.write ("Current temperature is: {:.2f} deg C".format(temp_city))
file.write('\n')
sname = file.write ('weather: '+weather_desc)
file.write('\n')
sname1 = 'humidity: '+str(hmdt)+'%'
file.write(sname1+'\n')
sname2 = 'wind speed: '+str(wind_spd)+'kmph'
file.write (sname2)
file.write('\n')
file.write (date_time)
file.close()
