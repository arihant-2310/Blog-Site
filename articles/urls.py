from django.urls import path
from . import views #from current directory import views.py file

urlpatterns = [
    path('',views.articles_list), #url to articles home page
]
