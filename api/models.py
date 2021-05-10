from django.db import models
from embed_video.fields import EmbedVideoField
import django_filters



class Launch(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    upcoming = models.BooleanField(blank = True, null = True)
    succeeded = models.BooleanField(blank = True, null = True)
    launch_year = models.IntegerField(blank = True, null = True)
    launch_date = models.DateTimeField(max_length=50, blank = True, null = True)
    description = models.CharField(max_length=500, blank = True, null = True)
    rocket = models.CharField(max_length=50, blank = True, null = True)
    launch_site = models.CharField(max_length=50, blank = True, null = True)
    slug = models.SlugField(default = 'test')
    image_url = models.CharField( max_length=50, blank = True, null = True)
    image_alt_url = models.CharField( max_length=50, blank = True, null = True)
    article_url = models.URLField( max_length=500, blank = True, null = True)
    wikipedia_url = models.URLField( max_length=500, blank = True, null = True)
    video = EmbedVideoField(blank = True, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
      verbose_name_plural = "launches"
