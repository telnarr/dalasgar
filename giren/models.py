from django.db import models


class giren(models.Model):
    san = models.IntegerField()

    def __str__(self):
        return str(self.san)
# Create your models here.
