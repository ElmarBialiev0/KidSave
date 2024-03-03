from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index_page, name='index_page'),
    path("buy/", buy_page, name='buy_page'),
    path("about/", about_page, name='about_page'),
]
