from django.db import models
from django.utils import timezone
from filer.fields.image import FilerImageField

import datetime

class ResearchBase(models.Model):
    pub_date = models.DateTimeField('date published')
    authors = models.CharField(max_length=200)
    year = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    image = FilerImageField()
    link = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Journal(ResearchBase):
    journal = models.CharField(max_length=200)
    abstract = models.TextField()
    citation = models.CharField(max_length=200)


class Encyclopedia_Chapter(ResearchBase):
    encyclopedia = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)


class Book(ResearchBase):
    publisher = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)