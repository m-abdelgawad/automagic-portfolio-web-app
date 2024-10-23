from django.contrib import admin
from .models import Skill, Configuration


# Register your models here.
@admin.register(Skill)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ['title', 'status', 'icon', 'description', 'order', ]

    list_filter = ['status', ]

    search_fields = ['title', 'status', 'icon', 'description', ]

    ordering = ['order', ]


@admin.register(Configuration)
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
