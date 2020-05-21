from django.contrib import admin
from django.urls import path
from . import views #from current directory import views.py file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about), #url to about page
    path('',views.homepage), #url to home page
]
