from django.db import models
from django.conf import settings
CHALLENGE_TYPE = (('TREE', 'TREE'), ('SANITATION',
                  'SANITATION'), ('OCEAN', 'OCEAN'))
# Create your models here.

User = settings.AUTH_USER_MODEL


class Contribution(models.Model):
    contributor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    location = models.TextField()
    number = models.PositiveBigIntegerField()
    picture = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)


class Challenge(models.Model):
    starts = models.DateTimeField(auto_now_add=True)
    challange_type = models.CharField(max_length=50, choices=CHALLENGE_TYPE)
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    contribution = models.ManyToManyField(Contribution)
    target = models.PositiveIntegerField()
