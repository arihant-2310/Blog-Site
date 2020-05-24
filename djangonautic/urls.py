from django.contrib import admin
from django.urls import path,include
from . import views #from current directory import views.py file
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as articles_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('articles/',include('articles.urls')),
    path('about/',views.about), #url to about page
    path('',articles_view.articles_list,name="home"), #url to home page
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
