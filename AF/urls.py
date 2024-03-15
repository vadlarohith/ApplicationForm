from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('App', views.Application, name='Application'),
    path('details', views.details, name='details'),
]