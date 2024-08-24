from django.db import models

class Courses(models.Model):
    price=models.DecimalField(default=0,decimal_places=2,max_digits=5)
    cname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    duration=models.TimeField()
    stcount=models.IntegerField()

    def __str__(self):
        return self.cname

class Meta:
    abstract=True



# Create your models here.
