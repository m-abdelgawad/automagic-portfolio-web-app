from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # Project views
    path('', views.contact, name='contact'),
]
