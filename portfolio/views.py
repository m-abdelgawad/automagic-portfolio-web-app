from django.shortcuts import render, get_object_or_404
from .models import Project, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count
from itertools import chain


# Define the number of elements in one page
page_elements_count = 6

# Define number of similar projects
similar_projects_count = 3


# Create your views here.
def portfolio_home(request, tag_slug=None, category_slug=None):

    project_list = Project.published.all().order_by('-complete_date')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        project_list = project_list.filter(skills__in=[tag])
    else:
        tag = None
        
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        project_list = project_list.filter(category__in=[category])
    else:
        category = None
        
    projects_count = project_list.count()

    # Pagination with page_elements_count per page
    paginator = Paginator(project_list, page_elements_count)

    # f the page parameter is not in the GET parameters of the request, we use
    # the default value 1 to load the first page of results.
    page_number = request.GET.get('page', 1)

    # Try get the requested page
    try:
        projects = paginator.page(page_number)

    # If the requests page is out of rangee, retrun the last page
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)

    # If the requests page is not an integer, return the first page
    except PageNotAnInteger:
        projects = paginator.page(1)

    return render(
        request,
        'portfolio/portfolio_home.html',
        {
            'projects': projects,
            'projects_count': projects_count,
            'tag': tag,
            'category': category,
        }
    )


def portfolio_project(request, project):

    project = get_object_or_404(Project, slug=project
                                , status=Project.Status.PUBLISHED)

    # List of similar projects

    # retrieve a Python list of IDs for the tags of the current project. The
    # values_list() QuerySet returns tuples with the values for the given
    # fields. We pass flat=True to it to get single values such as
    # [1, 2, 3, ...] instead of one-tuples such as [(1,), (2,), (3,) ...]
    project_skills_ids = project.skills.values_list('id', flat=True)

    # We get all projects that contain any of these tags, excluding the current
    # project itself.
    similar_projects = Project.published.filter(skills__in=project_skills_ids).exclude(id=project.id)

    # use the Count aggregation function to generate a calculated
    # field (same_tags) that contains the number of tags shared with all the
    # tags queried.
    # We order the result by the number of shared tags (descending order) and
    # by publish to display recent projects first for the projects with the same
    # number of shared tags. We slice the result to retrieve only the first
    # three projects.
    similar_projects = similar_projects.annotate(same_skills=Count('skills')) \
                        .order_by('-same_skills', '-complete_date')[:similar_projects_count]

    # Fill similar projects with normal projects; if the similar projects are less than
    # the required similar_projects_count
    if len(similar_projects) < similar_projects_count:
        extra_projects_count = similar_projects_count - len(similar_projects)
        extra_projects = Project.published.order_by('-complete_date').exclude(id=project.id) \
                          .exclude(id__in=similar_projects)[:extra_projects_count]
        similar_projects = list(chain(similar_projects, extra_projects))
    
    return render(
        request,
        'portfolio/portfolio_project.html',
        {
            'project': project,
            'similar_projects': similar_projects,
        }
    )
