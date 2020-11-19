from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class MyUser(AbstractUser):
    sodu = models.IntegerField(default=0)





# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.contrib.auth import get_user_model

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=255, default='')
#     city = models.CharField(max_length=100, default='')
#     phone = models.IntegerField(default=0)
#     sodu = models.FloatField(default=0)

# def create_profile(sender, **kwargs):
#     User = get_user_model()
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#     post_save.connect(create_profile, sender=User)

class Post(models.Model):
    title = models.CharField(max_length=21, blank=False, null=False)
    content = models.TextField(max_length=255, blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class HistoryModel(models.Model):
    title_history = models.CharField(default=User, max_length=255)
    his_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    clone_id = models.CharField(max_length=9999, default='')
    so_luong = models.CharField(max_length=9999, default='')
    time_pub = models.DateTimeField(auto_now_add=True, blank=True)
    list_clone = models.TextField(default='', max_length=9999)


    def __str__(self):
        return self.title_history




