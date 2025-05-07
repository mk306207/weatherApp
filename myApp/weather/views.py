from django.shortcuts import render, redirect
from django.contrib import messages
from apiKey import apiKey
import requests
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cleanJsonData(URL):
    response = requests.get(URL)
    response = response.json()
    cleaned_data = {
    "location":response["location"]["name"],
    "forecast":[
        {
            "date":day["date"][5:],
            "temp":day["day"]["avgtemp_c"],
            "windMAX":day["day"]["maxwind_kph"],
            "weatherIcon":day["day"]["condition"]["icon"]
        }
        for day in response["forecast"]["forecastday"]
    ]
    }
    return cleaned_data

def requestCity(city,request):
    apiURL = f'http://api.weatherapi.com/v1/forecast.json?key={apiKey}&q={city}&days=7&aqi=no&alerts=no'
    response = requests.get(apiURL)
    response = response.json()
    if "error" in response:
        messages.add_message(request, messages.ERROR, "Invalid city name")
        print("Invalid city name")
        return None
    else:
        print(response["location"]["name"])
        return response

def searchCity(request):
    if request.method == 'POST':
        city = request.POST.get("searchedCity")
        if city == "":
            pass
        else:
            data = requestCity(city,request)
            if data:
                return redirect(reverse('singleCity', args=[city]))
            else:
                messages.add_message(request, messages.ERROR, "Invalid city name")
                return redirect('searchCity')
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
    cleanedData = cleanJsonData(apiURL)
    print(cleanedData)
    data.append(cleanedData)
    
    #Hamburg
    apiURL = f'http://api.weatherapi.com/v1/forecast.json?key={apiKey}&q=Hamburg&days=7&aqi=no&alerts=no'
    cleanedData = cleanJsonData(apiURL)
    print(cleanedData)
    data.append(cleanedData)
    return JsonResponse(data,safe=False)

def singleCity(request,city):
    apiURL = f'http://api.weatherapi.com/v1/forecast.json?key={apiKey}&q={city}&days=7&aqi=no&alerts=no'
    cleanedData = cleanJsonData(apiURL)
    apiURL = f'http://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}&aqi=no'
    response = requests.get(apiURL)
    response = response.json()
    return render(request,"singleCity.html",{"data":cleanedData, "current":response})