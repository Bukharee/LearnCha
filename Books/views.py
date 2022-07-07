from django.shortcuts import render, get_object_or_404
from .models import Subject, Books, Answer
from django.contrib.auth.decorators import login_required
from .serializers import SubjectsSerializer, BooksSerializer, AnswersSerializer
from rest_framework import generics

# Create your views here.


def categories(request):
    """
    our home categories goes here
    1. Games
    2. Dictionary
    3. Books
    4. Quiz 
    5. Enpshyclopedia
    """
    pass


def subjects_list(request, quiz=False):
    if not quiz:
        "one two three"
        link = "grade"
    else:
        link = "quiz"
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {"subjects": subjects, "link": link})


@login_required
def books_list(request, subject_title):
    try:
        subject = get_object_or_404(Subject, slug=subject_title)
    except:
        return render(request, 'books_list.html', {"books": None, "message":
                                                   "not a valid subject"})
    else:
        books = Books.objects.filter(subject=subject, grade=request.user.grade)
        if books:
            return render(request, 'books_list.html', {
                "books": books, "message": "Valid Subject"})
        else:
            return render(request, 'books_list.html', {
                "books": books, "message": "No Book"})


@login_required
def quiz(request, subject_title):
    try:
        subject = get_object_or_404(Subject, slug=subject_title)
    except:
        return render(request, 'quiz.html', {"questions": None, "message":
                                             "not a valid subject"})
    else:
        questions = Answer.my_objects.get_random(subject=subject_title)
        return render(request, 'quiz.html', {"questions": questions})


@login_required
def encyclopedia(request):
    pass


# the api code starts here

class SubjectsListAPIView(generics.ListAPIView):
    queryset = subjects = Subject.objects.all()
    serializer_class = SubjectsSerializer
