from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # Use your custom admin site for the db1 admin interface
    path('blog/', views.blog, name='blog'),
    path('blogpost/<str:slug>/', views.blogpost, name='blogpost'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

