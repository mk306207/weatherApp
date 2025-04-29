from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("realtime-weather",views.realtime_weather,name="realtime_weather"),
]