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
    current_capacity = models.IntegerField(default=0, blank=True, null=True)
    rated_capacity = models.IntegerField(default=0, blank=True, null=True)

    def changethecapacity(self):
        self.current_capacity = (self.current_capacity + self.rated_capacity) / 2
        if self.current_capacity > 100:
            self.current_capacity = 100
        self.save()
        return self.current_capacity

    def changerating0(self):
        self.rated_capacity = 0
        self.save()
        return self.rated_capacity

    def changerating25(self):
        self.rated_capacity = 25
        self.save()
        return self.rated_capacity

    def changerating50(self):
        self.rated_capacity = 50
        self.save()
        return self.rated_capacity

    def changerating75(self):
        self.rated_capacity = 75
        self.save()
        return self.rated_capacity


    def changerating100(self):
        self.rated_capacity = 100
        self.save()
        return self.rated_capacity