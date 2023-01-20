from django.test import TestCase
from django.urls import resolve,reverse,path,include
from .urls import router
from .models import History,Studystate,Strong,StrongExp,STUDYSTATE
from rest_framework import status
from rest_framework.test import APITestCase
import json

# Create your tests here.

class IndexViewSetTests(APITestCase):    
    urlpatterns = [
        path('portfolio/api/index',include(router))
    ]
    def test_connect_endpoint(self):
        urls = [
            reverse('history-list'),
            reverse('studystate-list'),
            reverse('strong-list')
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_strong_encode(self):
        # data make
        s1 = Strong.objects.create(strong="aaa")
        s2 = Strong.objects.create(strong="bbb")
        s3 = Strong.objects.create(strong="ccc")
        se11 = StrongExp.objects.create(strong = s1,exp = "111")
        se12 = StrongExp.objects.create(strong = s1,exp = "112")
        se13 = StrongExp.objects.create(strong = s1,exp = "113")
        se21 = StrongExp.objects.create(strong = s2,exp = "121")
        se22 = StrongExp.objects.create(strong = s2,exp = "122")
        se23 = StrongExp.objects.create(strong = s2,exp = "123")
        se31 = StrongExp.objects.create(strong = s3,exp = "131")
        se32 = StrongExp.objects.create(strong = s3,exp = "132")
        se33 = StrongExp.objects.create(strong = s3,exp = "133")

        expected = json.dumps([
            {
                "strong":s1.__str__(),
                "exps":[
                    se11.__str__(),
                    se12.__str__(),
                    se13.__str__(),
                ]
            },
            {
                "strong":s2.__str__(),
                "exps":[
                    se21.__str__(),
                    se22.__str__(),
                    se23.__str__(),
                ]
            },
            {
                "strong":s3.__str__(),
                "exps":[
                    se31.__str__(),
                    se32.__str__(),
                    se33.__str__(),
                ]
            }
        ]).replace(" ","")

        # access
        url = reverse('strong-list')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'),expected)
    
    def test_history_encode(self):
        # data make
        h1 = History.objects.create(when="1",event="a",order=1)
        h2 = History.objects.create(when="2",event="b",order=2)
        expected = json.dumps([
            {"when":h1.when,"event":h1.event},
            {"when":h2.when,"event":h2.event},
        ]).replace(" ","")

        # access
        url = reverse('history-list')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'),expected)
    
    def test_studystate_encode(self):
        # data make
        s1 = Studystate.objects.create(state=STUDYSTATE[0][0],language="c",imgurl="http://a.com")
        s2 = Studystate.objects.create(state=STUDYSTATE[0][0],language="c++",imgurl="http://b.com")
        s3 = Studystate.objects.create(state=STUDYSTATE[1][0],language="c#",imgurl="http://c.com")
        s4 = Studystate.objects.create(state=STUDYSTATE[1][0],language="java",imgurl="http://d.com")
        s5 = Studystate.objects.create(state=STUDYSTATE[2][0],language="python",imgurl="http://e.com")
        s6 = Studystate.objects.create(state=STUDYSTATE[2][0],language="rust",imgurl="http://f.com")
        expected = json.dumps({
            "will":[
                {"imgurl":s1.imgurl},
                {"imgurl":s2.imgurl}
            ],
            "ing":[
                {"imgurl":s3.imgurl},
                {"imgurl":s4.imgurl}
            ],
            "can":[
                {"imgurl":s5.imgurl},
                {"imgurl":s6.imgurl}
            ]
        }).replace(" ","")
        # access
        url = reverse('studystate-list')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'),expected)