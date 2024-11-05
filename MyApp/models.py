from django.db import models

# Create your models here.

class Employee(models.Model):
        def nameFile(instance, filename):
                return '/'.join(['images', str(instance.name), filename])
        name = models.CharField(max_length = 255)
        hod = models.CharField(max_length=250)
        salary = models.IntegerField()
        picture = models.ImageField(upload_to=nameFile,blank=True)



# class Profile(models.Model):
#         def nameFile(instance, filename):
#                 return '/'.join(['images', str(instance.name), filename])
#         name = models.CharField(max_length = 255)
#         picture = models.ImageField(upload_to=nameFile,blank=True)
