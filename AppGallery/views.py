from django.shortcuts import render
from .models import SliderShowcaseApp, CounterUpItem


# Create your views here.
def apps_list(request):

    # Retrieve all objects with status "Published"
    counter_items = CounterUpItem.objects.filter(status=CounterUpItem.Status.PUBLISHED).order_by('order')

    apps_items = SliderShowcaseApp.objects.filter(status=CounterUpItem.Status.PUBLISHED).order_by('order')

    context = {
        'counter_items': counter_items,
        'apps_items': apps_items,
    }

    return render(request, 'AppGallery/web_apps_list.html', context)
