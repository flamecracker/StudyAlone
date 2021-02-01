from django.db import models

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL',unique=True)

    def __str__(self):
        return "%s %s" %(self.title, self.url)
# Create your models here.
