from pyexpat import model
from django.db import models
from account.models import UserAccount
# Create your models here.
BLOCK_TYPE= [
    ('Main Campus', 'Main Campus'),
    ('Clustor Campus', 'Clustor Campus'),
    ('Health Campus', 'Health Campus'),
    ('Butajera Campus', 'Butajera Campus'),
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
    Block_Capacity=models.IntegerField() 
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
    Stud_id=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    block=models.ForeignKey(Block,on_delete=models.CASCADE)
    room=models.ForeignKey(Dorm,on_delete=models.CASCADE)
    def __str__(self):
        return self.Stud_id

