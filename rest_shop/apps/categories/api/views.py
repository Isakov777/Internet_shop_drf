from rest_framework import generics
from rest_framework.serializers import Serializer
from apps.categories.api.serializers import CategorySerializer, CategoryDetailSerializer
from apps.categories.models import Category


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serilizer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer