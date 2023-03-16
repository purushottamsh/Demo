"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from client import views
from dj_rest_auth.views import LogoutView
from client.views import CustomLoginAPI



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.ClientListCreateAPIView.as_view(), name='client-list-create-api'),
    path('client/<int:pk>/', views.ClientRetrieveUpdateAPIView.as_view(), name='client-retrieve-update-api'),
    path('create/',views.UserViewSet.as_view({'get':'post'}),name='UserViewSet'),
    path('login/', CustomLoginAPI.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),


]