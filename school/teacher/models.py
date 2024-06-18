from django.db import models

# Create your models here.
class Teacher(models.Model):
     first_name = models.CharField(max_length = 20)
     last_name = models.CharField(max_length = 20)
     email = models.EmailField()
     country = models.CharField(max_length = 20)
     date_of_birth = models.DateField()
     code = models.PositiveSmallIntegerField()
     place_of_birth = models.CharField(max_length = 10)
     nationality = models.CharField(max_length = 15)
     gender = models.CharField(max_length = 13)
     course = models.CharField(max_length = 10)



     def __str__(self):
        return f"{self.first_name} {self.last_name}"