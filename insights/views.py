from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from portfolio.models import Project
from blog.models import Post
from datetime import datetime, timedelta


# Create your views here.
def insights_home(request):
    # --------------------- Start project categories ----------------- #

    categories_dict = {}

    projects_categories_labels = []

    projects_categories_data = []

    projects_queryset = Project.published.all().order_by('complete_date')

    for project in projects_queryset:
        if project.category.title not in categories_dict:
            categories_dict[project.category.title] = 1
        else:
            categories_dict[project.category.title] += 1

    # Resort by value
    categories_dict = {k: v for k, v in sorted(
        categories_dict.items(), key=lambda item: item[1], reverse=True
    )}

    for key, value in categories_dict.items():
        projects_categories_labels.append(key)
        projects_categories_data.append(value)

    # --------------------- End project categories ----------------- #

    # --------------------- Start project count ----------------- #
    project_count = projects_queryset.count()
    # --------------------- End project count ----------------- #

    # --------------------- Start articles count ----------------- #
    posts_count = Post.published.all().count()
    # --------------------- End articles count ----------------- #

    # ---------------- Start projects in last 30 days count ----------------- #
    last_month = datetime.today() - timedelta(days=30)
    month_items = projects_queryset.filter(complete_date__gte=last_month).count()
    # ---------------- End projects in last 30 days count ----------------- #

    # --------------------- Start projects timeline ----------------- #
    projects_timeline_labels = ['', ]
    projects_timeline_data = [0, ]
    projects_timeline_dict = {}

    for project in projects_queryset:
        project_date = project.complete_date.strftime("%Y-%m")
        if project_date not in projects_timeline_dict:
            projects_timeline_dict[project_date] = 1
        else:
            projects_timeline_dict[project_date] += 1

    for key, value in projects_timeline_dict.items():
        projects_timeline_labels.append(key)
        projects_timeline_data.append(value)

    # --------------------- End projects timeline ----------------- #

    # ---------------- Start Projects Skills ----------------- #
    skills_dict = {}
    skills_labels = []
    skills_data = []

    for project in projects_queryset:
        project_skills = project.skills.names()

        for skill in project_skills:
            skill = skill.strip()
            if skill not in skills_dict:
                skills_dict[skill] = 1
            else:
                skills_dict[skill] += 1

    # Resort by value
    skills_dict = {k: v for k, v in sorted(
        skills_dict.items(), key=lambda item: item[1], reverse=True
    )}

    for key, value in skills_dict.items():
        skills_labels.append(key)
        skills_data.append(value)

    # ---------------- End Projects Skills ----------------- #

    return render(request, 'insights/insights_home.html', {
        'projects_categories_labels': projects_categories_labels,
        'projects_categories_data': projects_categories_data,
        'project_count': project_count,
        'posts_count': posts_count,
        'month_items': month_items,
        'projects_timeline_labels': projects_timeline_labels,
        'projects_timeline_data': projects_timeline_data,
        'skills_labels': skills_labels,
        'skills_data': skills_data,
    })
