"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
<<<<<<< HEAD
#from django.contrib import admin
from django.urls import path, include

urlpatterns = [
=======
from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('core', include('core.urls')),
>>>>>>> 0438d5d890ff30646664be8b5b74678c6a4c8a6b
    path('product', include('product.urls'))
]
