from django.contrib import admin
from django.urls import path
from .views import name, cricketer,flag

urlpatterns = [
    path('name',name,name="quiz"),
    path('cricketer',cricketer,name="cricketer"),
    path('flag',flag,name="flag"),
]
