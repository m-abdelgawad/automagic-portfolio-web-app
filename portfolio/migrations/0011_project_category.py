# Generated by Django 4.1.4 on 2023-03-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0010_category_remove_project_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="portfolio_categories",
                to="portfolio.category",
            ),
        ),
    ]
