from django import template
from ..models import Configuration


register = template.Library()


@register.simple_tag
def home_configs():
    return Configuration.load()
