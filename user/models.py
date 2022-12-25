from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class RoleType(Enum):
    Mail_Man = 1
    Technician = 2
    Admin = 3


#extend for the Original User
class User(AbstractUser):


    class RoleType2(models.IntegerChoices):
        Mail_Man = 1, "Mail_Man"
        Technician = 2, "Technician"
        Admin = 3, 'Admin'

    age = models.IntegerField(null= True, blank = True )
    City = models.CharField(max_length=100,null= True, blank = True)
    Full_address = models.CharField(max_length=100,null= True, blank = True)
    Postal_Code = models.IntegerField(null= True, blank = True)
    Phonenumber = models.PositiveIntegerField(null= True, blank = True)
    Role = models.PositiveIntegerField(null= True, choices=RoleType2.choices)

    def __str__(self):
        if self.Full_address:
            return self.Full_address
        return 'no_adress'
        
    def get_type(self):
        for choice in self.RoleType2:
            if self.type == choice.value:
                return choice.label
        return 'NO TYPE'



#class Staffmember(models.Model):
    #user = models.OneToOneField(NewUser, on_delete = models.CASCADE)
    #Role = models.CharField(max_length=100,null= True, blank = True)
    #Rank = models.IntegerField(null= True, blank = True)


    #def __str__(self) :
        #return self.user.username

#@receiver(post_save, sender = User)
#def create_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Staffmember.objects.create(user = instance)        