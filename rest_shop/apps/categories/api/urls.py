from typing import ValuesView
from django.urls import path
from apps.categories.api import views

urlpatterns = [
    path('', views.CategoryAPIView.as_view(), name='category_api'),
    path('create/', views.CategoryCreateAPIView.as_view(), name='category_create_api'),
    path('update/<int:pk>/', views.CategoryUpdateAPIView.as_view(), name = 'category_update_api'),
    path('delete/<int:pk>/', views.CategoryDeleteAPIView.as_view(), name='category_delete_api'),
    path('detail/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category_detail_api'),
]