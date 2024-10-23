from django.urls import path
from . import views


app_name = 'custom_auth'

urlpatterns = [
    path('', views.authenticate_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]