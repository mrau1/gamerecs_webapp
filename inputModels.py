from django.db import models

class input(models.Model):
    entry = models.CharField(max_length=500)
    def __str__(self):
        return t"(self.entry)"