from rest_framework import generics, permissions
from apps.products.api import serializers
from apps.products.models import Product, ProductImage


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_class = [permissions.IsAuthenticated]


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class  = serializers.ProductDetailSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class ProductImageCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
