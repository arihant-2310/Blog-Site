from django.contrib import admin
from django.urls import path,include
from . import views #from current directory import views.py file
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
    path('about/',views.about), #url to about page
    path('',views.homepage), #url to home page
]

urlpatterns += staticfiles_urlpatterns()
