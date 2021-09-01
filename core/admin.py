from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser


# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
