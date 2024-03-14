# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'roll', 'session', 'is_staff', 'is_superuser')
#     list_filter = ('is_staff', 'is_superuser', 'session')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': ('roll', 'session')}),
#         ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'roll', 'session', 'password1', 'password2', 'is_staff', 'is_superuser'),
#         }),
#     )
#     search_fields = ('username', 'roll')
#     ordering = ('username',)

# admin.site.register(CustomUser, CustomUserAdmin)
