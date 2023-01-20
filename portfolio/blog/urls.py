from django.urls import path,include
from .views import BlogView

app_name = 'blog'

urlpatterns = [
    path('',BlogView.as_view())
]