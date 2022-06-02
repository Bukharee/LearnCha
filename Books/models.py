from django.db import models
from Users.models import GRADE_CHOICES
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

    def __str__(self) -> str:
        return super().__str__(self.title)

    class Meta:
         verbose_name_plural = "Quizzes"

class Answer(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct = models.CharField(max_length=600)
    first_option =  models.CharField(max_length=600)
    second_option =  models.CharField(max_length=600)
    third_option =  models.CharField(max_length=600)
