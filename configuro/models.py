from django.db import models


# Create your models here.
class Configuration(models.Model):

    class TitleSeperator(models.TextChoices):
        DASH = '-', '-'
        PIPE = '|', '|'
        COMMA = ',', ','

    website_title = models.CharField(max_length=250, null=True, blank=True)
    title_seperator = models.CharField(
        max_length=250,
        choices=TitleSeperator.choices,
        default=TitleSeperator.DASH,
        null=True,
        blank=True,
    )
    website_description = models.TextField(null=True, blank=True)
    website_author = models.CharField(max_length=250, null=True, blank=True)
    featured_image = models.FileField(upload_to='uploads/site_configuration/', null=True, blank=True)
    fav_icon = models.FileField(upload_to='uploads/site_configuration/', null=True, blank=True)
    logo = models.FileField(upload_to='uploads/site_configuration/', null=True, blank=True)

    footer_copyright = models.CharField(max_length=250, null=True, blank=True)

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Configurations'

    def save(self, *args, **kwargs):
        # Override the save method to ensure only one row is saved
        self.pk = 1
        super(Configuration, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Return the singleton instance
        obj, created = cls.objects.get_or_create(pk=1)

        if obj.active:
            return obj
        else:
            return {}

    def __str__(self):
        return 'Site Configurations'
