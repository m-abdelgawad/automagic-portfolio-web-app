from django.shortcuts import render


# Create your views here.
def error_400(request, exception):
    data = {}
    return render(request, 'friendly_errors/400.html', data)


def error_403(request, exception):
    data = {}
    return render(request, 'friendly_errors/403.html', data)


def error_404(request, exception):
    data = {}
    return render(request, 'friendly_errors/404.html', data)


def error_500(request, *args, **argv):
    data = {}
    return render(request, 'friendly_errors/500.html', data)