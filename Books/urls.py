from importlib.resources import path
from django.urls import path
from .views import books_list, subjects_list, quiz, SubjectsListAPIView, books_list_api

app_name = "books"

urlpatterns = [
    path('subjects/', subjects_list, name="subjects"),
    path('subjects/<slug:quiz>/', subjects_list, name="subject_quiz"),
    path('grade/<slug:subject_title>/', books_list, name="books"),
    path('quiz/<slug:subject_title>/', quiz, name="quiz"),
    path('subjects-list', SubjectsListAPIView.as_view(), name="subjects-list"),
    path('books-list/<slug:subject_title>',
         books_list_api, name="books-list"),
]
