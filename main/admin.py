from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Mash)
admin.site.register(Cities)
admin.site.register(Users)
admin.site.register(Stations)



# Register your models here.
