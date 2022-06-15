from unicodedata import name
from django.urls import path
from .views import home, profile, contact, about
from .views import SignUpView

app_name = "users"

urlpatterns = [
    path('', home, name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", profile, name="profile"),
    path("about/", about, name="about"),
    path('contact/', contact, name="contact"),
]
