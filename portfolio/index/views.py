from django.shortcuts import render
from .models import History,Studystate,Strong
from .serializers import HistorySerializer,StudystateSerializer,StrongSerializer
from rest_framework import viewsets
# Create your views here.


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = History.objects.all().order_by('order')
    serializer_class = HistorySerializer

class StudystateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Studystate.objects.all()
    serializer_class = StudystateSerializer

class StrongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Strong.objects.all()
    serializer_class = StrongSerializer