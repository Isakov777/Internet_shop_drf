from re import T
from django.db import models 
from django.db.models import fields
from rest_framework import serializers
from apps.products.models import Product, ProductImage
from apps.users.api.serializers import UserSerializer
from apps.categories.models import Category

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many = True, read_only = True)
    user = UserSerializer(read_only = True)

    class Meta:
        model = Product
        fields = (
            'id', 'user', 'title', 'description', 'price', 'quantity', 'category', 'product_image'
        )

class ProductDetailSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many = True, read_only = True)
    Category = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = Product
        fields = (
            'id', 'user', 'title', 'description', 'price', 'quantity', 'category', 'product_image', 'is_stock', 'Category'
        )