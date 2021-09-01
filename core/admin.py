from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser


# Register your models here.
class UserModel(UserAdmin):
    # list_display = ('data', 'descricao', 'pu_compra')
    # list_filter = ('descricao',)
    pass


admin.site.register(CustomUser, UserModel)
