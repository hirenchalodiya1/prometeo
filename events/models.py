from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name="Event Name", unique=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Cover Image")
    rulebook = models.FileField(upload_to="rulebooks/", null=True, blank=True, verbose_name="Rulebook File")
    prize = models.IntegerField(verbose_name="Prize Money (Rs.)", null=True, blank=True)
    description = models.TextField(max_length=5000, verbose_name="Event Description")
    date = models.DateField(verbose_name="Event Date")
    time = models.TimeField(null=True, blank=True, verbose_name="Event Time")
    venue = models.CharField(max_length=50, null=True, blank=True, verbose_name="Event Venue")
    
