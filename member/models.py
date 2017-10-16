from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# MemberModel
class Member(models.Model):
    code = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    name = models.CharField(max_length=200)
    about = models.TextField(null=True)
    point = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name