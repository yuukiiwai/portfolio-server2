from django.test import TestCase,Client
from django.urls import resolve,reverse,path,include
from rest_framework import status
from rest_framework.test import APITestCase
from .views import BlogView
import json
# Create your tests here.
class BlogAPITests(TestCase):
    client = Client()
    def test_connect_endpoint(self):
        response = self.client.get("/portfolio/api/blog/",HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)