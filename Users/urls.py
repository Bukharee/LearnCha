from unicodedata import name
from django.urls import path
from .views import home
from .views import SignUpView

urlpatterns = [
  path('', home, name='home'),
  path("signup/", SignUpView.as_view(), name="signup"),


]