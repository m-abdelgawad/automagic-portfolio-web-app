from django import template
from ..models import Post, AuthorBox


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.simple_tag
def author_box():
    return AuthorBox.load()
