from django.db import models

# Create your models here.
class Course(models.Model):
     course_name = models.CharField(max_length = 20)
     course_objective = models.CharField(max_length = 20)
     course_duration = models.DurationField()
     course_students = models.CharField(max_length = 20)
     course_level = models.PositiveSmallIntegerField()
     course_description= models.TextField(max_length = 30)
     course_title = models.CharField(max_length = 10)
     course_teacher = models.CharField(max_length = 15)
     course_id = models.PositiveSmallIntegerField()
     course_resources = models.CharField(max_length = 19)



     def __str__(self):
        return f"{self.course_name} {self.course_level}"