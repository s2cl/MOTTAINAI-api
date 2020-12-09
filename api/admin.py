from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django_boost.admin import register_all
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.

admin.site.register(User, UserAdmin)
register_all(models)