from django.shortcuts import render
from rest_framework.views import APIView
import urllib.request
import re
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BlogView(APIView):
    def get(self,request,format=None):
        req = urllib.request.Request("https://note.com/y_u_k_i_open/rss")
        the_page = ""
        ret = list()
        with urllib.request.urlopen(req) as response:
            the_page_b = response.read()
            the_page = the_page_b.decode('utf-8')
        for m in re.finditer(r'.*<link>https://note.com/y_u_k_i_open/n/(.*)</link>.*',the_page,re.MULTILINE):
            ret.append({"id":m.groups()[0]})
        # print(ret)
        return Response(ret,status.HTTP_200_OK)