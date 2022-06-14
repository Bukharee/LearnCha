from tkinter.messagebox import QUESTION
from django.db import models
from Users.models import GRADE_CHOICES
from random import randint
from django.db.models.aggregates import Count
# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.title)


class Books(models.Model):
    title = models.CharField(max_length=250)
    book = models.FileField()
    cover = models.ImageField()
    grade = models.CharField(choices=GRADE_CHOICES, max_length=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name_plural = "Books"


class Quiz(models.Model):
    question = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.question)

    class Meta:
        verbose_name_plural = "Quizzes"


class AnswerManager(models.Manager):
    def get_random(self, subject):
        """
        used to fetch atmost 10 question of a
        particular subject
        """
        questions = []
        subjects_questions = self.filter(question__subject=subject).count()
        if subjects_questions > 10:
            while len(questions) <= 10:
                try:
                    count = self.aggregate(count=Count('id'))['count']
                    random_index = randint(0, count - 1)
                    question = self.filter(question__subject=subject)[
                        random_index]
                    if question and question not in questions:
                        questions.append(question)
                except ValueError:
                    return None
            return questions
        else:
            questions = self.filter(question__subject=subject)
            return questions


class Answer(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct = models.CharField(max_length=600)
    first_option = models.CharField(max_length=600)
    second_option = models.CharField(max_length=600)
    third_option = models.CharField(max_length=600)
    my_objects = AnswerManager()

    def __str__(self) -> str:
        return str(self.first_option)
