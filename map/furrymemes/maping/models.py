from django.db import models


class Group(models.Model):
    group_name = models.TextField(max_length=20, blank=True)
