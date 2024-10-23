from django.urls import path
from . import views


app_name = 'app_gallery'

urlpatterns = [
    path('', views.apps_list, name='app_gallery'),
]
