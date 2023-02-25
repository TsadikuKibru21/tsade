
from pyexpat import model
from django.db import models

# Create your models here.
BLOCK_TYPE= [
    ('Single-Block', 'Single Block'),
    ('4-Sieded-Block', '4_Sided Block'),
    ]
PURPOSE= [
    ('Males Block', 'Males Block'),
    ('Females Block', 'Females Block'),
    ]
CHOICES = [
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    ]
Gend=[
    ('Male','Male'),
    ('Female','Female'),
]

class Block(models.Model):
    Block_name=models.CharField(max_length=100)
    Block_type=models.CharField(max_length=150 , choices=BLOCK_TYPE)
    Block_purpose=models.CharField(max_length=100, choices=PURPOSE) 
    Status=models.CharField(max_length=150 , choices=CHOICES)
    def __str__(self):
        return self.Block_name
class Dorm(models.Model):
    Block=models.ForeignKey(Block,on_delete=models.CASCADE)
    Dorm_name=models.CharField(max_length=100)
    Capacity=models.CharField(max_length=10)
    Status=models.CharField(max_length=150 , choices=CHOICES)
    def __str__(self):
        return self.Dorm_name
    

class Placement(models.Model):
    Stud_id=models.CharField(max_length=100)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,choices=Gend)
    collage=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    batch=models.CharField(max_length=100)
    block=models.CharField(max_length=100)
    room=models.CharField(max_length=100)
    def __str__(self):
        return self.Stud_id