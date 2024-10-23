from django.db import models


# Create your models here.
class SliderShowcaseApp(models.Model):

    # Adding a status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)

    short_description = models.TextField()

    long_description = models.TextField()

    button_text = models.CharField(max_length=250)

    button_icon = models.CharField(max_length=250)

    button_url = models.CharField(max_length=500)

    image = models.ImageField(upload_to="app_image")

    order = models.PositiveIntegerField()

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    def __str__(self):
        return self.title


class CounterUpItem(models.Model):

    # Adding a status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)

    count_number = models.CharField(max_length=250)

    icon = models.CharField(max_length=250)

    order = models.PositiveIntegerField()

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    def __str__(self):
        return self.title
