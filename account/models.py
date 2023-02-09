from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Role(models.Model):
    R_name=models.CharField(max_length=200,default='Student')
    def __str__(self):
        return self.R_name
class User(models.Model):
    GENDER_CHOICES=(
        ('M','Male'),
        ('F', 'Female')
    )
    Stud_or_not=(
        ('yes','Student'),
        ('no', 'Not Student')
    )
    #Role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    Id_no=models.CharField(max_length=200,null=False)
    FirstName=models.CharField(max_length=100,null=False)
    LastName=models.CharField(max_length=100,null=False)
    Gender=models.CharField(choices=GENDER_CHOICES, max_length=6, null=False,default='M')
    phone_no=models.IntegerField(null=False)
    stream=models.CharField(max_length=200, null=True,blank=True)
    collage=models.CharField(max_length=200, null=True,blank=True)
    Department=models.CharField(max_length=200, null=True,blank=True)
    Year_of_Student=models.CharField(max_length=50, null=True,blank=True)
    Emergency_responder_name=models.CharField(max_length=200,null=True,blank=True)
    Emergency_responder_address=models.CharField(max_length=200,null=True,blank=True)
    Emergency_responder_phone_no=models.CharField(max_length=13, null=True,blank=True)
    Employee_id=models.CharField(max_length=50, null=True,blank=True)
    Student_or_Not=models.CharField(max_length=50,null=False,choices=Stud_or_not)
    def __str__(self):
        return self.FirstName
    
class UserAccount(AbstractUser):
      Role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
      username=models.CharField(max_length=200,null=True,unique=True)
      password=models.CharField(max_length=500)
      User=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

