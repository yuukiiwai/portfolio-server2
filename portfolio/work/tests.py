from django.test import TestCase
from django.urls import resolve,reverse,path,include
from .urls import router
from .models import Work
from rest_framework import status
from rest_framework.test import APITestCase
import json

# Create your tests here.

class IndexViewSetTests(APITestCase):    
    urlpatterns = [
        path('portfolio/api/work',include(router))
    ]
    def test_connect_endpoint(self):
        url = reverse('work-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_work_encode(self):
        # data make
        w1 = Work.objects.create(title="a",url="http://a.com",slide="http://a.com/slide")
        w2 = Work.objects.create(title="b",url="http://b.com",slide="http://b.com/slide")
        
        expected = json.dumps([
            {"title":w1.title,"url":w1.url,"slide":w1.slide},
            {"title":w2.title,"url":w2.url,"slide":w2.slide},
        ]).replace(" ","")

        # access
        url = reverse('work-list')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'),expected)