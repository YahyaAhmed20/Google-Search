from django.urls import path
from . import views


app_name='google'

urlpatterns = [
    path('',views.google,name='google'),
    path('', views.home_view, name='home'),  # Default home page

    path('gmail/', views.gmail_view, name='gmail'),
    path('images/', views.images_view, name='images'),
]