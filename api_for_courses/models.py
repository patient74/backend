from django.db import models

class Course(models.Model):
   Title = models.CharField(max_length=300)
   Course_code = models.CharField(max_length=100)
   Description = models.CharField(max_length=500)


class Course_instance(models.Model):
   Year = models.CharField(max_length=10)
   Semester = models.CharField(max_length=10)
   Course_id = models.CharField(max_length=10)

# Create your models here.
