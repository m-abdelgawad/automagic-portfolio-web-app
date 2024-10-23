from django.contrib import admin
from .models import SliderShowcaseApp, CounterUpItem


# Register your models here.
@admin.register(SliderShowcaseApp)
class SliderShowcaseAppAdmin(admin.ModelAdmin):

    list_display = ['title', 'short_description', 'status', 'order', ]

    list_filter = ['status', 'order', ]

    search_fields = ['title', 'short_description', 'long_description', ]

    ordering = ['order']


@admin.register(CounterUpItem)
class CounterUpItemAdmin(admin.ModelAdmin):

    list_display = ['title', 'count_number', 'icon', 'status', 'order', ]

    list_filter = ['status', 'order', ]

    search_fields = ['title', ]

    ordering = ['order']
