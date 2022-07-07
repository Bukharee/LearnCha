from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from rest_framework.decorators import (
    authentication_classes, permission_classes, api_view)
from rest_framework import permissions, authentication, generics
from .serializers import (CreateChallangeSerializer,
                          ContributionSerializer, ViewChallangesSerializer)
from .models import Challange
# Create your views here.


class CreateChallangeAPIView(generics.CreateAPIView):
    queryset = Challange.objects.all()
    serializer_class = CreateChallangeSerializer


class ListChallangesAPIView(generics.ListAPIView):
    queryset = Challange.objects.all()
    serializer_class = ViewChallangesSerializer
