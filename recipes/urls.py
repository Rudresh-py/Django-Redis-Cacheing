from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [

    path('',home , name='home'),
    path('create', create_recipe, name='create'),
    path('<int:id>',show , name='show'),
    
]