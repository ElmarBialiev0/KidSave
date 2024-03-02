from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('index/', index_page, name='index_page')
]
