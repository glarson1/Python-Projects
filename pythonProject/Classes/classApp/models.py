from django.db import models

# Create your models here.
class djangoClasses(models.Model):  #created a class
    title = models.CharField(max_length=60, default="", blank=True, null=False) #string
    courseNumber = models.IntegerField(default=0, blank=True, null=False) #integer
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)#string
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2) #float

    objects = models.Manager() #manages are objectsS