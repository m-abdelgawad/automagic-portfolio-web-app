from django.db import models


# Create your models here.
class Skill(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    description = models.TextField()
    order = models.IntegerField()

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    def __str__(self):
        return self.title


class Configuration(models.Model):

    hero_intro = models.CharField(max_length=250, null=True, blank=True)
    hero_title = models.CharField(max_length=250, null=True, blank=True)
    hero_sub_title = models.CharField(max_length=250, null=True, blank=True)
    hero_paragraph = models.TextField(null=True, blank=True)
    hero_button_text = models.CharField(max_length=250, null=True, blank=True)
    hero_button_icon = models.CharField(max_length=250, null=True, blank=True)
    hero_button_url = models.CharField(max_length=250, null=True, blank=True)
    hero_animation_file = models.FileField(upload_to='uploads/home_configuration/', null=True, blank=True)

    skills_section_title = models.CharField(max_length=250, null=True, blank=True)

    projects_section_title = models.CharField(max_length=250, null=True, blank=True)
    projects_button_text = models.CharField(max_length=250, null=True, blank=True)
    projects_button_icon = models.CharField(max_length=250, null=True, blank=True)

    blog_section_title = models.CharField(max_length=250, null=True, blank=True)
    blog_button_text = models.CharField(max_length=250, null=True, blank=True)
    blog_button_icon = models.CharField(max_length=250, null=True, blank=True)

    contact_section_title = models.CharField(max_length=250, null=True, blank=True)
    contact_section_paragraph = models.TextField(null=True, blank=True)
    contact_button_text = models.CharField(max_length=250, null=True, blank=True)
    contact_button_icon = models.CharField(max_length=250, null=True, blank=True)

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
        return 'Home Page Configurations'
