from turtle import title
from django.shortcuts import render, get_object_or_404
from .models import Subject, Books, Answer
from django.contrib.auth.decorators import login_required


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


def subjects_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {"subjects": subjects})


@login_required
def books_list(request, subject_title):
    print("nan")
    try:
        subject = get_object_or_404(Subject, slug=subject_title)
    except:
        return render(request, 'books_list.html', {"books": None, "message":
                                                   "not a valid subject"})
    else:
        books = Books.objects.filter(subject=subject, grade=request.user.grade)
        print(books)
        return render(request, 'books_list.html', {"books": books, "message": "Valid Subject"})


@login_required
def quiz(request, subject_title):
    try:
        subject = get_object_or_404(Subject, slug=subject_title)
    except:
        return render(request, 'quiz.html', {"questions": None, "message":
                                             "not a valid subject"})
    else:
        questions = Answer.my_objects.get_random()
        return render(request, 'quiz.html', {"questions": questions})
