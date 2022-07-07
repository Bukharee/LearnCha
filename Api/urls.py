from django.urls import path
from .views import (ProductMixinApiView, api_home, ProductDetailAPIView,
                    ProductCreateAPIView, ProductListAPIView,
                    ProductListCreateAPIView, product_alt_view,  ProductDeleteAPIView,
                    ProductUpdateAPIView)
from rest_framework.authtoken.views import obtain_auth_token


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
    path("auth", obtain_auth_token)
]
