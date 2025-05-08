from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from unittest.mock import patch, Mock

class TestHomePage(SimpleTestCase):
    
    def testHomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def testSearch(self):
        response = self.client.get('/searchCity')
        self.assertEqual(response.status_code, 200)
        
    def testSingleCity(self):
        response = self.client.get('/searchCity/Warsaw')
        self.assertEqual(response.status_code, 200)

class TestAPICall(TestCase):
    def setUp(self):
        self.client = Client()
        
    @patch('weather.views.requests.get')
    def testRealtimeWeather(self,mockGet):
        mockResponse1 = Mock()
        mockResponse1.json.return_value={'location':{"name":"Honolulu"}}
        mockResponse2 = Mock()
        mockResponse2.json.return_value={'location':{"name":"NewYork"}}
        mockGet.side_effect = [mockResponse1,mockResponse2]
        response = self.client.get(reverse('realtime_weather'))
        self.assertEqual(response.status_code,200)
        response = response.json()
        self.assertEqual(response[0]["location"]["name"],"Honolulu")
        self.assertEqual(response[1]["location"]["name"],"NewYork")
        
    @patch('weather.views.requests.get')
    def testForecastWeather(self, mockGet):
        mockResponse1 = Mock()
        mockResponse1.json.return_value={
                                            "location": {
                                                "name": "Honolulu"
                                            },
                                            "forecast": {
                                                "forecastday": [
                                                {
                                                    "date": "2025-05-08",
                                                    "date_epoch": 1746662400,
                                                    "day": {
                                                        "maxtemp_c": 17.4,
                                                        "maxtemp_f": 63.4,
                                                        "mintemp_c": 5.7,
                                                        "mintemp_f": 42.3,
                                                        "avgtemp_c": 11.5,
                                                        "avgtemp_f": 52.6,
                                                        "maxwind_mph": 9.4,
                                                        "maxwind_kph": 15.1,
                                                        "totalprecip_mm": 0.03,
                                                        "totalprecip_in": 0.0,
                                                        "totalsnow_cm": 0.0,
                                                        "avgvis_km": 10.0,
                                                        "avgvis_miles": 6.0,
                                                        "avghumidity": 64,
                                                        "daily_will_it_rain": 0,
                                                        "daily_chance_of_rain": 0,
                                                        "daily_will_it_snow": 0,
                                                        "daily_chance_of_snow": 0,
                                                        "condition": {
                                                            "text": "Partly Cloudy ",
                                                            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                                                            "code": 1003
                                                        },
                                                        "uv": 1.4
                                                    }
                                                },
                                                {
                                                    "date": "2025-05-09",
                                                    "date_epoch": 1746662400,
                                                    "day": {
                                                        "maxtemp_c": 27.4,
                                                        "maxtemp_f": 93.4,
                                                        "mintemp_c": 4.7,
                                                        "mintemp_f": 65.3,
                                                        "avgtemp_c": 77.5,
                                                        "avgtemp_f": 123.6,
                                                        "maxwind_mph": 123.4,
                                                        "maxwind_kph": 123.1,
                                                        "totalprecip_mm": 0.03,
                                                        "totalprecip_in": 0.0,
                                                        "totalsnow_cm": 0.0,
                                                        "avgvis_km": 10.0,
                                                        "avgvis_miles": 6.0,
                                                        "avghumidity": 64,
                                                        "daily_will_it_rain": 0,
                                                        "daily_chance_of_rain": 0,
                                                        "daily_will_it_snow": 0,
                                                        "daily_chance_of_snow": 0,
                                                        "condition": {
                                                            "text": "Partly Cloudy ",
                                                            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                                                            "code": 1003
                                                        },
                                                        "uv": 1.4
                                                    }
                                                }
                                                ]
                                            }
                                            }
        mockResponse2 = Mock()
        mockResponse2.json.return_value = {
                                            "location": {
                                                "name": "New York"
                                            },
                                            "forecast": {
                                                "forecastday": [
                                                {
                                                    "date": "2025-05-08",
                                                    "date_epoch": 1746662400,
                                                    "day": {
                                                    "maxtemp_c": 17.4,
                                                    "maxtemp_f": 63.4,
                                                    "mintemp_c": 5.7,
                                                    "mintemp_f": 42.3,
                                                    "avgtemp_c": 11.5,
                                                    "avgtemp_f": 52.6,
                                                    "maxwind_mph": 9.4,
                                                    "maxwind_kph": 15.1,
                                                    "totalprecip_mm": 0.03,
                                                    "totalprecip_in": 0.0,
                                                    "totalsnow_cm": 0.0,
                                                    "avgvis_km": 10.0,
                                                    "avgvis_miles": 6.0,
                                                    "avghumidity": 64,
                                                    "daily_will_it_rain": 0,
                                                    "daily_chance_of_rain": 0,
                                                    "daily_will_it_snow": 0,
                                                    "daily_chance_of_snow": 0,
                                                    "condition": {
                                                        "text": "Partly Cloudy ",
                                                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                                                        "code": 1003
                                                    },
                                                    "uv": 1.4
                                                    }
                                                },
                                                {
                                                    "date": "2025-05-09",
                                                    "date_epoch": 1746662400,
                                                    "day": {
                                                    "maxtemp_c": 27.4,
                                                    "maxtemp_f": 93.4,
                                                    "mintemp_c": 4.7,
                                                    "mintemp_f": 65.3,
                                                    "avgtemp_c": 77.5,
                                                    "avgtemp_f": 123.6,
                                                    "maxwind_mph": 123.4,
                                                    "maxwind_kph": 123.1,
                                                    "totalprecip_mm": 0.03,
                                                    "totalprecip_in": 0.0,
                                                    "totalsnow_cm": 0.0,
                                                    "avgvis_km": 10.0,
                                                    "avgvis_miles": 6.0,
                                                    "avghumidity": 64,
                                                    "daily_will_it_rain": 0,
                                                    "daily_chance_of_rain": 0,
                                                    "daily_will_it_snow": 0,
                                                    "daily_chance_of_snow": 0,
                                                    "condition": {
                                                        "text": "Partly Cloudy ",
                                                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                                                        "code": 1003
                                                    },
                                                    "uv": 1.4
                                                    }
                                                }
                                                ]
                                            }
                                        }
        mockGet.side_effect = [mockResponse1,mockResponse2]
        response = self.client.get(reverse('forecast_weather'))
        response = response.json()
        print(response)
        self.assertEqual(response[0]["location"],"Honolulu")
        self.assertEqual(response[1]["location"],"New York")
        self.assertEqual(response[0]["forecast"][0]["date"],"05-08")
        self.assertEqual(response[1]["forecast"][0]["date"],"05-08")