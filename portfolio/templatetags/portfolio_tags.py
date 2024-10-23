from django import template
from ..models import Project

"""
Each module that contains template tags needs to define a variable called
register to be a valid tag library. This variable is an instance of
template.Library(), and it’s used to register the template tags and filters
of the application.
"""
register = template.Library()

"""
we have defined a tag called total_posts with a simple Python function. We
have added the @register.simple_tag decorator to the function, to register it 
as a simple tag. Django will use the function’s name as the tag name. If you 
want to register it using a different name, you can do so by specifying a name 
attribute, such as @register.simple_tag(name='my_tag')
"""


@register.simple_tag
def total_projects():
    """
    a simple template tag that returns the number of posts published in the blog.
    """
    return Project.published.count()
