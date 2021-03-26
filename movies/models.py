from django.db import models

# Create your models here.
class Actor(models.Model):
    act_id=models.IntegerField()
    act_fname=models.CharField(max_length=20)
    act_lname=models.CharField(max_length=20)
    act_gender=models.IntegerField()

    def __str__(self):
           return self.act_id

    class Meta:
         ordering=('act_id',)

class movie(models.Model):
    mov_id=models.IntegerField()
    mov_title=models.CharField(max_length=50)
    mov_year=models.IntegerField()

    def __str__(self):
        return self.mov_title
class Meta:
    ordering=('mov_title',)