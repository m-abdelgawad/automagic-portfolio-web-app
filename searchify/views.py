from django.shortcuts import render
from .forms import SearchForm
from django.db.models import Q
from blog.models import Post
from portfolio.models import Project


# Create your views here.
def post_search(request):

    form = SearchForm()

    query = None
    blog_results = []
    portfolio_results = []

    if 'query' in request.GET:

        form = SearchForm(request.GET)

        if form.is_valid():

            query = form.cleaned_data['query']

            blog_results = Post.published.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()

            portfolio_results = Project.published.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(skills__name__icontains=query) |
                Q(category__title__icontains=query) |
                Q(developer__icontains=query)
            ).distinct()

    return render(
        request,
        'searchify/search.html',
        {
            'form': form,
            'query': query,
            'blog_results': blog_results,
            'portfolio_results': portfolio_results,
        }
    )
