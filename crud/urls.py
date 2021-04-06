from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('', views.index , name='home'),
    path('read', views.read , name='read'),
    path('update', views.update , name='update'),
    path('delete', views.delete , name='delete'),
    path('updateform', views.updateform , name='updateform')
]