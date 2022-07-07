from typing import List
from django.urls import path
from .views import (CreateChallangeAPIView,
                    ListChallangesAPIView, ChallangeDetailAPIView, ContibuteAPIView)
urlpatterns = [
    path("create-challange", CreateChallangeAPIView.as_view(),
         name="create_challange"),
    path("list-challanges", ListChallangesAPIView.as_view(),
         name="list_challanges"),

    path("challange-detail/<int:pk>", ChallangeDetailAPIView.as_view(),
         name="view_challange"),

    path("contribute/", ContibuteAPIView.as_view(),
         name="contribute"),
]
