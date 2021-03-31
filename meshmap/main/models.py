from django.db import models

class Contact(models.Model):
    time = models.DateTimeField()
    source_name = models.CharField(max_length=30)
    source_lat = models.DecimalField(max_digits=9, decimal_places=6)
    source_lon = models.DecimalField(max_digits=9, decimal_places=6)
    contact_name = models.CharField(max_length=30)
    contact_lat = models.DecimalField(max_digits=9, decimal_places=6)
    contact_lon = models.DecimalField(max_digits=9, decimal_places=6)
