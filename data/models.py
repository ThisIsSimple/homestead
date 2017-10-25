from django.db import models
from django.utils import timezone

class Data(models.Model):
    client_id = models.CharField(max_length=32)
    module_id = models.CharField(max_length=255, default=0)
    temp = models.FloatField()
    hum = models.FloatField()
    soil = models.FloatField()
    light = models.FloatField()
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()