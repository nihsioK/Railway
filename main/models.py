from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.template.context_processors import request


# from user_profile.models import Profile


class Cities(models.Model):
    name_city = models.CharField(max_length=100, blank=True)
    Users = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_city


class Stations(models.Model):
    accept_train_time_begin = models.DateTimeField()
    accept_train_time_end = models.DateTimeField()
    stations = models.OneToOneField(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return self.stations.name_city


class Users(models.Model):
    name = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Mash(models.Model):
    name = models.CharField(max_length=100)
    job_start = models.BooleanField()
    med_check = models.BooleanField(default=False, blank=True)
    accept_train = models.BooleanField(blank=True)
    station = models.ForeignKey(Stations, on_delete=models.CASCADE, null=True, blank=True)
    pass_train = models.BooleanField(default=False, blank=True)
    job_end = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name

'''''''''
class Accept(models.Model):
    pass_train = models.BooleanField()

    def __str__(self):
        return self.name

# Create your models here.
'''''''''''
"""""""""
class Mashinist(models.Model):
    name = models.CharField(max_length=100)
    job_start = models.CharField('job_start', choices=choices, widget=forms.RadioSelect(), max_length=50)
    med_check = models.CharField('med_check', max_length=50)
    accept_train = models.CharField('accept_train', max_length=50)
    accept_train_time_begin = models.DateTimeField()
    accept_train_time_end = models.DateTimeField()
    stations = models.CharField('stations', max_length=50)
    pass_train = models.CharField('pass_train', max_length=50)
    job_end = models.CharField('job_end', max_length=50)

    def __str__(self):
        return self.name
"""""""""
