from django.contrib.auth.models import User, Group
from ihair.catalog.models import Category, Product
from rest_framework import permissions, generics
from ihair.catalog.serializers import UserSerializer, GroupSerializer, CategorySerializer, ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   

class ProductList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  