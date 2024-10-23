from django.shortcuts import render

# Create your views here.
from .models import Skill
from portfolio.models import Project
from blog.models import Post
from AppGallery.models import SliderShowcaseApp

# Create your views here.
def home(request):
    projects = Project.published.all().filter(featured=True)
    posts = Post.published.all().filter(featured=True)
    skills = Skill.objects.all().filter(status=Skill.Status.PUBLISHED).order_by('order')
    return render(
        request,
        'home/home.html',
        {
            'projects': projects,
            'skills': skills,
            'posts': posts,
        }
    )
