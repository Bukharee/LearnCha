from gettext import install
from pyexpat import model
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework import generics, authentication, permissions
from rest_framework.mixins import ListModelMixin
from .permissions import IsStaffPermission
from .authentication import BaseAuthentication

# Create your views here.


# def api_home(request, *args, **kwargs):
"""
trying out api with raw django
"""
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     data["headers"] = dict(request.headers)
#     data["content_type"] = request.content_type
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     """
#     trying out api with raw django and getting some data from database
#     """
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, exclude=['id'])
#     return JsonResponse(data)

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     trying out api with raw django and getting some data from database
#     """
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data)
#     return Response(data)

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     trying out api with raw django and getting some data from database
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    trying out api with raw django and getting some data from database
    """
    serialiser = ProductSerializer(data=request.data)
    if serialiser.is_valid(raise_exception=True):
        # instance = serialiser.save() #in serializer you cant do commit=False
        print(serialiser.data)
        return Response(serialiser.data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
        print(serializer)
        return super().perform_create(serializer)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsStaffPermission]
    authentication_classes = [
        BaseAuthentication, authentication.SessionAuthentication]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return None
        return  qs.filter(user=user)


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None):
    if request.method == "POST":
        serializer = ProductSerializer
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # perform create here

    if request.method == "GET":
        # perform list view, detail view
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data)
        # list view
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        return super().perform_update(serializer)


class ProductDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class ProductMixinApiView(ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
