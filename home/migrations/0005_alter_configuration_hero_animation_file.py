# Generated by Django 4.1.4 on 2024-12-14 07:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_configuration_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='hero_animation_file',
            field=cloudinary.models.CloudinaryField(default='defaultvalue', max_length=255),
            preserve_default=False,
        ),
    ]
