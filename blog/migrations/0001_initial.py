# Generated by Django 4.1.4 on 2023-05-06 16:31

import ckeditor_uploader.fields
import django.utils.timezone
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_title', models.CharField(blank=True, max_length=250, null=True)),
                ('author_name', models.CharField(blank=True, max_length=250, null=True)),
                ('author_job_title', models.CharField(blank=True, max_length=250, null=True)),
                ('about_author', models.TextField(blank=True, null=True)),
                ('social_1_icon', models.CharField(blank=True, max_length=250, null=True)),
                ('social_1_icon_color', models.CharField(blank=True, max_length=250, null=True)),
                ('social_1_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('social_2_icon', models.CharField(blank=True, max_length=250, null=True)),
                ('social_2_icon_color', models.CharField(blank=True, max_length=250, null=True)),
                ('social_2_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('social_3_icon', models.CharField(blank=True, max_length=250, null=True)),
                ('social_3_icon_color', models.CharField(blank=True, max_length=250, null=True)),
                ('social_3_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('author_photo', models.FileField(blank=True, null=True, upload_to='uploads/blog_configuration/')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Author Box',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='blog_covers')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                (
                'status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('featured', models.BooleanField()),
                ('author',
                 models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.',
                                                         through='taggit.TaggedItem', to='taggit.Tag',
                                                         verbose_name='Tags')),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                           to='blog.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish'], name='blog_post_publish_bb7600_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-created'], name='blog_commen_created_79f39f_idx'),
        ),
    ]
