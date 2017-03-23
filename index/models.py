from django.db import models
from django.utils import timezone
from datetime import datetime
from django.template import Template, Context


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Library(models.Model):
    title = models.CharField(max_length=200)
    hours = models.TextField()

    def dayofweek(self):
        dt = datetime.today()
        return dt.strftime('%A')

class Floor(models.Model):
    libname = models.CharField(max_length=200, default='')
    floor_number = models.IntegerField(default=1, blank=True, null=True)
    total_capacity = models.IntegerField(default=0, blank=True, null=True)
    current_capacity = models.IntegerField(default=0, blank=True, null=True)
    rated_capacity = models.IntegerField(default=0, blank=True, null=True)
    num_ratings = models.IntegerField(default = 0, blank=True,null=True)

    def changethecapacity(self, rate):
        self.num_ratings = self.num_ratings + 1
        self.total_capacity = float(float(self.total_capacity) + float(self.rated_capacity))
        self.current_capacity = self.total_capacity / self.num_ratings
        self.save()

    def changerating(self, rate):
        self.rated_capacity = rate
        self.save()