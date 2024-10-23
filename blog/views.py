from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.views.decorators.http import require_POST
from taggit.models import Tag
"""
This is the Count aggregation function of the Django ORM. This function will 
allow you to perform aggregated counts of tags. django.db.models includes the 
following aggregation functions:
• Avg: The mean value
• Max: The maximum value
• Min: The minimum value
• Count: The total number of objects
"""
from django.db.models import Count
from itertools import chain


# Define the number of elements in one page
page_elements_count = 6

# Define number of similar posts
similar_posts_count = 3


# Create your views here.
def blog_list(request, tag_slug=None):

    post_list = Post.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
        
    posts_count = post_list.count()

    # Pagination with page_elements_count per page
    paginator = Paginator(post_list, page_elements_count)

    # f the page parameter is not in the GET parameters of the request, we use
    # the default value 1 to load the first page of results.
    page_number = request.GET.get('page', 1)

    # Try get the requested page
    try:
        posts = paginator.page(page_number)

    # If the requests page is out of range, retrun the last page
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    # If the requests page is not an integer, return the first page
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(
        request,
        'blog/blog_home.html',
        {
            'posts': posts,
            'posts_count': posts_count,
            'tag': tag,
        }
    )


def blog_post(request, post_slug):

    post = get_object_or_404(
        Post,
        slug=post_slug,
        status=Post.Status.PUBLISHED
    )
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'GET':

        # Form for users to comment
        form = CommentForm()

    else:

        # Define a comment variable with the initial value None. This variable will
        # be used to store the comment object when it gets created.
        comment = None

        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            # Assign the post attribute of the comment to the current post
            comment.post = post

            # Save the comment to the database
            comment.save()

    # List of similar posts

    # retrieve a Python list of IDs for the tags of the current post. The
    # values_list() QuerySet returns tuples with the values for the given
    # fields. We pass flat=True to it to get single values such as
    # [1, 2, 3, ...] instead of one-tuples such as [(1,), (2,), (3,) ...]
    post_tags_ids = post.tags.values_list('id', flat=True)

    # We get all posts that contain any of these tags, excluding the current
    # post itself.
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)

    # use the Count aggregation function to generate a calculated
    # field (same_tags) that contains the number of tags shared with all the
    # tags queried.
    # We order the result by the number of shared tags (descending order) and
    # by publish to display recent posts first for the posts with the same
    # number of shared tags. We slice the result to retrieve only the first
    # three posts.
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                        .order_by('-same_tags', '-created')[:similar_posts_count]

    # Fill similar posts with normal posts; if the similar posts are less than
    # the required similar_posts_count
    if len(similar_posts) < similar_posts_count:
        extra_posts_count = similar_posts_count - len(similar_posts)
        extra_posts = Post.published.order_by('-created').exclude(id=post.id)\
                          .exclude(id__in=similar_posts)[:extra_posts_count]
        similar_posts = list(chain(similar_posts, extra_posts))

    return render(
        request,
        'blog/blog_post.html',
        {
            'post': post,
            'form': form,
            'comments': comments,
            'similar_posts': similar_posts,
        }
    )
