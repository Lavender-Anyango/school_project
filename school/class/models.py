from django.db import models

# Create your models here.
class Class(models.Model):
    class_id = models.SmallIntegerField(max_length=5)
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=12)
    capacity = models.SmallIntegerField(max_length=10)
    color = models.CharField(max_length=20)
    building_material = models.CharField(max_length=255, default='Unknown')
    building_material = models.CharField(max_length=30)
    code = models.PositiveSmallIntegerField()
    sitting_arrangement = models.FileField()
    electronics = models.CharField()
    class_temperature = models.CharField(max_length=255, default='Unknown')



    



    def __str__(self):
        return f'{self.name} {self.capacity}'
        