from django.shortcuts import render
from rest_framework import viewsets
from .models import Work
from .serializers import WorkSerializer

class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer