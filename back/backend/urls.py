"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from controlo_voo import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'avioes', views.AviaoView, 'aviao')
router.register(r'companhias', views.CompanhiaView, 'companhia')
router.register(r'nacionais', views.NacionalView, 'nacional')
router.register(r'internacionais', views.InternacionalView, 'internacional')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/createNacional/', views.CreateNacional.as_view(), name='createNacional'),
    path('api/createInternacional/', views.CreateInternacional.as_view(), name='createInternacional'),
    path('api/createAviao/', views.CreateAviao.as_view(), name='createAviao'),
    path('api/createCompanhia/', views.CreateCompanhia.as_view(), name='createCompanhia'),
    path('api/avioes/<int:pk>/', views.delete_aviao, name='delete_aviao'),
    path('api/internacionais/<int:pk>/', views.delete_internacional, name='delete_internacional'),
    path('api/nacionais/<int:pk>/', views.delete_nacional, name='delete_nacional'),
    path('api/companhias/<int:pk>/', views.delete_companhia, name='delete_companhia'),
]
