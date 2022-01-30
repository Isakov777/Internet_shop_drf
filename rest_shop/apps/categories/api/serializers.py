from rest_framework import serializers
from django.db.models import fields
from apps.categories.models import Category
from apps.products.models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title', 'parent')




class CategoryDetailSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Category
        fields = ('id','title', 'parent')