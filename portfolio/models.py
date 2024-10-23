from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from crum import get_current_user


class Category(models.Model):

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


# Creating model managers
class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=Project.Status.PUBLISHED)


class SkillsTaggableManager(TaggableManager):
    def __init__(self, **kwargs):
        kwargs['verbose_name'] = 'Skills'
        super().__init__(**kwargs)


# Create your models here.
class Project(models.Model):
    """
    Add Project table to the database
    """

    # Adding a status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250, unique=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='portfolio_posts',
        blank=True,
        null=True,
        editable=False,
    )

    developer = models.CharField(max_length=250)

    complete_date = models.DateField()

    skills = SkillsTaggableManager(blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='portfolio_categories',
        blank=True,
        null=True,
        editable=True,
    )

    project_url = models.CharField(max_length=250)

    # body = models.TextField()
    body = RichTextUploadingField()  # CKEditor Rich Text Field

    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    featured = models.BooleanField()

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    # Defining a default sort order
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_project', args=[self.slug])

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.author = user
        super(Project, self).save(*args, **kwargs)
