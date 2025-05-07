# Weather app - Mateusz Kolber  
## Before you start  
There is an additional file called apiKey.py where I store my API key from www.weatherapi.com. Please remember that, if you won't put there your API key the application won't work!  
## Functions  
### home(request)  
Starting functions, renders home.html.  
### cleanJsonData(URL)  
URL - API call for example : http://api.weatherapi.com/v1/current.json?key=25457a4ba53f4494aaa114255252904&q=London&aqi=no  
This functions helps with forecast API call, because weatherAPI gives me a really long json file with many unneccessary data, so I created this function which helps me keep my code clean.  
### requestCity(city,request)  
city - string, which contains name of the city we are looking for, for example Warsaw,  
Same as function described above, it gets API call for this certain city given in a function argument.  
### searchCity(request)  
Function used when user wishes to search for his city of choice. It gets city name by method POST and tries to link it to any data provided by weatherAPI. If it fails website informs about it and lets user try again.  
### realtime_weather(request)  
Gets current temperature and wind speed for deafult cities (Gliwice and Hamburg)  
### forecast_weather(request)  
Gets weather forecast for next 7 days for deafult cities.  
### singleCity(request,city)  
city - string, which contains name of the city we are looking for, for example Warsaw,  
Gets weather forecast for next 7 days for chosen city.   