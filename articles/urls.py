from django.urls import path
from django.conf.urls import url
from . import views #from current directory import views.py file

app_name = 'articles'

urlpatterns = [
    path('',views.articles_list,name="list"), #url to articles home page
    url(r'^(?P<slug>[\w-]+)/$', views.article_details,name="detail"), #match article slug
]
