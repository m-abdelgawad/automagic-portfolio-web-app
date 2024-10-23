"""automagic_developer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import auth_gates.views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from portfolio.sitemaps import ProjectSitemap
from home.sitemaps import StaticSitemap


sitemaps = {
    'posts': PostSitemap,
    'projects': ProjectSitemap,
    'static': StaticSitemap,
}


urlpatterns = [

    path('admin/login/', auth_gates.views.authenticate_user),
    path('admin/', admin.site.urls),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # My applications URLs
    path('', include('home.urls', namespace='home')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('apps/insights_dashboard/', include('insights.urls', namespace='insights')),
    path('auth/', include('auth_gates.urls', namespace='auth_gates')),
    path('search/', include('searchify.urls', namespace='searchify')),
    path('app_gallery/', include('AppGallery.urls', namespace='app_gallery')),

    # Installed Applications URLs
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# Specify URL for static files e.g. images. We have added the static() helper
# function to serve media files with the Django development server during
# development (that is when the DEBUG setting is set to True).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Change admin panel title
admin.site.site_header = 'AutoMagic Developer'


handler400 = 'friendly_errors.views.error_400'
handler403 = 'friendly_errors.views.error_403'
handler404 = 'friendly_errors.views.error_404'
handler500 = 'friendly_errors.views.error_500'
