# Generated by Django 4.1.4 on 2023-03-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0009_alter_project_skills"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=250, unique=True)),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.RemoveField(
            model_name="project",
            name="category",
        ),
    ]
