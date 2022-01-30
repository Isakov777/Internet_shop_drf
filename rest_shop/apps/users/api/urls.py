from django.urls import path
from apps.users.api import views

urlpatterns = [
    path('', views.UserAPIView.as_view(), name='user_api'),
    path('current_user/', views.current_user, name='current_user'),
    path('detail/<int:pk>/', views.UserDetailAPIView.as_view(), name='detail_user')
]