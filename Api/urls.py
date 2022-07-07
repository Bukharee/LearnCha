from django.urls import path
from .views import (ProductMixinApiView, api_home, ProductDetailAPIView,
                    ProductCreateAPIView, ProductListAPIView,
                    ProductListCreateAPIView, product_alt_view,  ProductDeleteAPIView,
                    ProductUpdateAPIView)
from rest_framework.authtoken.views import obtain_auth_token
from Books.views import SubjectsListAPIView, books_list_api, quiz_api_view


from Climate.views import (CreateChallangeAPIView,
                           ListChallangesAPIView, ChallangeDetailAPIView, ContibuteAPIView)

from Dictionary.views import dictionary_search_api

urlpatterns = [
    path('', api_home, name="api_home"),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name="product_detail"),
    path("product/", ProductCreateAPIView.as_view(), name="create_product"),
    path("product/list", ProductMixinApiView.as_view(), name="list_products"),
    path("product/list-or-create", ProductListCreateAPIView.as_view(),
         name="list_or_create_products"),
    path("product/alt-view/<int:pk>",
         product_alt_view, name="proiduct_alt_view"),
    path("product/alt-view",
         product_alt_view, name="proiduct_alt_view"),
    path("product/update/<int:pk>",
         ProductUpdateAPIView.as_view(), name="update_product"),
    path("product/delete/<int:pk>",
         ProductDeleteAPIView.as_view(), name="delete_product"),
    path("auth", obtain_auth_token),

    # real urls
    # books app urls
    path('subjects-list', SubjectsListAPIView.as_view(), name="subjects-list"),
    path('books-list/<slug:subject_title>',
         books_list_api, name="books-list"),
    path('questions-list/<slug:subject_title>',
         quiz_api_view, name="questions_list"),
    # climate challange
    path("create-challange", CreateChallangeAPIView.as_view(),
         name="create_challange"),
    path("list-challanges", ListChallangesAPIView.as_view(),
         name="list_challanges"),

    path("challange-detail/<int:pk>", ChallangeDetailAPIView.as_view(),
         name="view_challange"),

    path("contribute/", ContibuteAPIView.as_view(),
         name="contribute"),
    # dictionary
    path('word', dictionary_search_api,
         name="dictionary_search_api"),
]
