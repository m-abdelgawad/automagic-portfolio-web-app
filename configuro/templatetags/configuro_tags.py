from django import template
from ..models import Configuration
from blog.models import Post
from portfolio.models import Project, Category


register = template.Library()


@register.simple_tag
def site_configs():
    return Configuration.load()


@register.simple_tag
def latest_posts():
    return Post.objects.filter(status='PB').order_by('-created')[:2]


@register.simple_tag
def latest_projects():
    return Project.objects.filter(status='PB').order_by('-created')[:5]


@register.simple_tag
def project_categories():
    return Category.objects.all()
