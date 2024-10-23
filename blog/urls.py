from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_home'),
    path('tag/<slug:tag_slug>/', views.blog_list, name='blog_list_by_tag'),
    path('<slug:post_slug>/', views.blog_post, name='blog_post'),
]
