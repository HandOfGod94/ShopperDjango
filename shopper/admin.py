from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """Display as list for user table"""
    list_display = ('username', 'password', 'gender',
                    'type_of_user', 'is_active')

admin.site.register(User, UserAdmin)
