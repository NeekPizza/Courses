from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Courses(models.Model):
    course_name = models.CharField(max_length=45, blank=True, null=True)
    course_description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
