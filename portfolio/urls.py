from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Project views
    path('', views.portfolio_home, name='portfolio_home'),
    path('skill/<slug:tag_slug>/', views.portfolio_home, name='portfolio_home_by_tag'),
    path('category/<slug:category_slug>/', views.portfolio_home, name='portfolio_home_by_category'),
    path('<slug:project>/', views.portfolio_project, name='portfolio_project'),
]
