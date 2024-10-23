from django.db import models
from django.urls import reverse
from crum import get_current_user
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


# Creating model managers
class BlogPublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here.
class Post(models.Model):
    """
    Add Post table to the database
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
        related_name='blog_posts',
        blank=True,
        null=True,
        editable=False,
    )

    body = RichTextUploadingField()  # CKEditor Rich Text Field

    cover = models.ImageField(upload_to="blog_covers", null=True, blank=True)

    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    tags = TaggableManager(blank=True)

    featured = models.BooleanField()

    objects = models.Manager()  # The default manager.
    published = BlogPublishedManager()  # Our custom manager.

    # Defining a default sort order
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_post', args=[self.slug])

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.author = user

        try:
            old_image = Post.objects.get(pk=self.pk).cover_image
        except:
            old_image = None

        super(Post, self).save(*args, **kwargs)

        if old_image:
            if self.cover != old_image:
                old_image.delete(save=False)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return "Comment by {0} on {1}".format(
            self.name, self.post
        )


class AuthorBox(models.Model):

    box_title = models.CharField(max_length=250, null=True, blank=True)

    author_name = models.CharField(max_length=250, null=True, blank=True)
    author_job_title = models.CharField(max_length=250, null=True, blank=True)
    about_author = models.TextField(null=True, blank=True)

    social_1_icon = models.CharField(max_length=250, null=True, blank=True)
    social_1_icon_color = models.CharField(max_length=250, null=True, blank=True)
    social_1_url = models.CharField(max_length=1000, null=True, blank=True)
    social_2_icon = models.CharField(max_length=250, null=True, blank=True)
    social_2_icon_color = models.CharField(max_length=250, null=True, blank=True)
    social_2_url = models.CharField(max_length=1000, null=True, blank=True)
    social_3_icon = models.CharField(max_length=250, null=True, blank=True)
    social_3_icon_color = models.CharField(max_length=250, null=True, blank=True)
    social_3_url = models.CharField(max_length=1000, null=True, blank=True)

    author_photo = models.FileField(
        upload_to='uploads/blog_configuration/', null=True, blank=True
    )

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Author Box'

    def save(self, *args, **kwargs):
        # Override the save method to ensure only one row is saved
        self.pk = 1
        super(AuthorBox, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Return the singleton instance
        obj, created = cls.objects.get_or_create(pk=1)

        if obj.active:
            return obj
        else:
            return {}

    def __str__(self):
        return 'Author Box Configurations'
