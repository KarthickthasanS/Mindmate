from django.urls import path
from . import views

urlpatterns = [
    path("aichat/",views.aichat,name="aichat"),
    path("chat_response/",views.chat_response,name="chat_response"),
    path("update_url/",views.update_url,name="update_url"),
    
]
