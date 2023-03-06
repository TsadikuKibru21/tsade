from django.db import models
from account.models import UserAccount
from StudentDean.models import Block
# Create your models here.
class ProctorSchedule(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    Block=models.ForeignKey(Block,on_delete=models.CASCADE)
    # date=models.DateField()
    # time=models.TimeField()
    def __str__(self):
        return self.user