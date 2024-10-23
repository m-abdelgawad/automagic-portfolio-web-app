from django.contrib import admin

from .models import Post, Comment, AuthorBox


# Customizing how models are displayed
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        return (
            'title',
            'slug',
            'body',
            'tags',
            'cover',
            'publish',
            'featured',
            'status',
        )

    def Tags(self, post):
        tags = []
        for tag in post.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)

    list_display = ['title', 'publish', 'Tags', 'status', 'author', 'featured', ]

    list_filter = ['status', 'publish', 'featured', ]

    search_fields = ['title', 'body']

    prepopulated_fields = {'slug': ('title',)}

    date_hierarchy = 'publish'

    ordering = ['-publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'post', 'created', 'active']

    list_filter = ['active', 'created', 'updated', ]

    search_fields = ['name', 'email', 'body']

    ordering = ['-created']


@admin.register(AuthorBox)
class SiteConfigurationAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # Check if there are any existing rows in the model
        count = self.model.objects.count()

        # If there are existing rows, don't allow adding new rows
        if count > 0:
            return False

        # If there are no existing rows, allow adding new rows
        return True

    def has_delete_permission(self, request, obj=None):
        return False
