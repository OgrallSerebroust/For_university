"""Fifth_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('data_page.html', views.data_page),
    path('insert_page.html', views.insert_page),
    path('add_theatres_data/', views.add_theatres_data),
    path('add_shows_data/', views.add_shows_data),
    path('add_visitors_data/', views.add_visitors_data),
    path('edit_theatre/<int:id_theatre>/', views.edit_theatre),
    path('delete_theatre/<int:id_theatre>/', views.delete_theatre),
    path('edit_show/<int:id_show>/', views.edit_show),
    path('delete_show/<int:id_show>/', views.delete_show),
    path('edit_visitor/<int:id_visitor>/', views.edit_visitor),
    path('delete_visitor/<int:id_visitor>/', views.delete_visitor),
]
