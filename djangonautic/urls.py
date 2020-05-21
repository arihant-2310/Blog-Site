from django.contrib import admin
from django.urls import path,include
from . import views #from current directory import views.py file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
    path('about/',views.about), #url to about page
    path('',views.homepage), #url to home page
]
