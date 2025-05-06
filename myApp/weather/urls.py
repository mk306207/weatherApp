from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("searchCity",views.searchCity,name="searchCity"),
    path("realtime-weather",views.realtime_weather,name="realtime_weather"),
    path("forecast-weather",views.forecast_weather,name="forecast_weather"),
]