from django.contrib import admin
from .models import Project, Category
from django.db.models import Count


# Customizing how models are displayed
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        return (
            'title',
            'slug',
            'developer',
            'complete_date',
            'skills',
            'category',
            'project_url',
            'body',
            'publish',
            'featured',
            'status',
        )

    def Skills(self, project):
        tags = []
        for tag in project.skills.all():
            tags.append(str(tag))
        return ', '.join(tags)

    list_display = ['title', 'category', 'Skills', 'status', 'author', 'complete_date', 'featured', ]

    list_filter = ['status', 'featured', ]

    search_fields = ['title', 'body', 'category', 'skills']

    prepopulated_fields = {'slug': ('title',)}

    # raw_id_fields = ['author']

    date_hierarchy = 'publish'

    ordering = ['-complete_date']

    # fieldsets = (
    #     ('Project Information', {
    #         'fields': (
    #
    #         )
    #     }),
    #     ('Additional Information', {
    #         'fields': (
    #
    #         )
    #     }),
    # )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug', 'projects_count']

    list_filter = ['title', 'slug', ]

    search_fields = ['title', 'slug']

    prepopulated_fields = {'slug': ('title',)}

    def projects_count(self, obj):
        return Project.objects.filter(category=obj).count()
