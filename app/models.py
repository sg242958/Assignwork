from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Score(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.student
        