from importlib.resources import path
from django.urls import path
from .views import books_list, subjects_list, quiz

urlpatterns = [
    path('subjects/', subjects_list, name="subjects"),
    path('grade/<slug:subject_title>/', books_list, name="books"),
    path('quiz/<slug:subject_title>/', quiz, name="quiz"),
]