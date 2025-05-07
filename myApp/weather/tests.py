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