from django.urls import path
from . import views

app_name = 'insights'

urlpatterns = [
    path('', views.insights_home, name='insights_home'),
]
