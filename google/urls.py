from django.urls import path
from . import views


app_name='google'

urlpatterns = [
    path('',views.google,name='google'),
    
]