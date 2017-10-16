from django.utils import timezone
from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=254)

    created_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name
