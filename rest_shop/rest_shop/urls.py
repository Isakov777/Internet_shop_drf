"""rest_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls.conf import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.users.api.urls')),
    path('products/', include('apps.products.api.urls')),
    path('categories/', include('apps.categories.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_update_pair_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('base-auth', include('rest_framework.urls'))
]
