from django.urls import path
from .views import search

app_name = "dictionary"

urlpatterns = [path('', search, name="search")]