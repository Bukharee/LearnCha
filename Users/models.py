from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


# Create your models here.

GRADE_CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),)
class User(AbstractUser):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    grade = models.CharField(choices=GRADE_CHOICES, max_length=50)
    nation = CountryField(blank_label='select country')