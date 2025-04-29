from django.shortcuts import render
from apiKey import apiKey
import requests
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
    
    print(locations);return JsonResponse(locations,safe=False)