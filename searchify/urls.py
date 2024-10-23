from django.urls import path
from . import views


app_name = 'searchify'

urlpatterns = [
    path('', views.post_search, name='post_search'),
]
