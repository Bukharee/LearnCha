from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import (CreateChallangeSerializer,
                          ContributionSerializer, ViewChallangesSerializer)
from .models import Challange, Contribution
from .mixins import AuthPermMixin
# Create your views here.


class CreateChallangeAPIView(generics.CreateAPIView, AuthPermMixin):
    queryset = Challange.objects.all()
    serializer_class = CreateChallangeSerializer


class ListChallangesAPIView(generics.ListAPIView):
    queryset = Challange.objects.all()
    serializer_class = ViewChallangesSerializer


class ChallangeDetailAPIView(generics.RetrieveAPIView, AuthPermMixin):
    queryset = Challange.objects.all()
    serializer_class = ViewChallangesSerializer
    lookup_field = "pk"


class ContibuteAPIView(generics.CreateAPIView, AuthPermMixin):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
