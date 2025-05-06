from django.shortcuts import render
from apiKey import apiKey
import requests
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def searchCity(request):
    return render(request,'searchCity.html')

def realtime_weather(request):
    locations = []
    #Gliwice
    apiURL = f'http://api.weatherapi.com/v1/current.json?key={apiKey}&q=Gliwice&aqi=no'
    response = requests.get(apiURL)
    locations.append(response.json())
    
    #Hamburg
    apiURL = f'http://api.weatherapi.com/v1/current.json?key={apiKey}&q=Hamburg&aqi=no'
    response = requests.get(apiURL)
    locations.append(response.json())
    
    return JsonResponse(locations,safe=False)

def forecast_weather(request):
    data = []
    #Gliwice
    apiURL = f'http://api.weatherapi.com/v1/forecast.json?key={apiKey}&q=Gliwice&days=7&aqi=no&alerts=no'
    response = requests.get(apiURL)
    response = response.json()
    cleaned_data = {
    "location":response["location"]["name"],
    "forecast":[
        {
            "date":day["date"],
            "temp":day["day"]["avgtemp_c"],
            "windMAX":day["day"]["maxwind_kph"],
            "weatherIcon":day["day"]["condition"]["icon"]
        }
        for day in response["forecast"]["forecastday"]
    ]
    }
    data.append(cleaned_data)
    
    #Hamburg
    apiURL = f'http://api.weatherapi.com/v1/forecast.json?key={apiKey}&q=Hamburg&days=7&aqi=no&alerts=no'
    response = requests.get(apiURL)
    response = response.json()
    cleaned_data = {
    "location":response["location"]["name"],
    "forecast":[
        {
            "date":day["date"],
            "temp":day["day"]["avgtemp_c"],
            "windMAX":day["day"]["maxwind_kph"],
            "weatherIcon":day["day"]["condition"]["icon"]
        }
        for day in response["forecast"]["forecastday"]
    ]
    }
    data.append(cleaned_data)

    return JsonResponse(data,safe=False)