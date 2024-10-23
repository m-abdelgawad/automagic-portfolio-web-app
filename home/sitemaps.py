from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'home:home',
            'contact:contact',
            'insights:insights_home',
            'todowoo:signup_user',
            'todowoo:login_user',
            'todowoo:home',
            'auth_gates:login',
        ]

    def location(self, item):
        return reverse(item)
