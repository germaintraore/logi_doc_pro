from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'role', 'is_active', 'is_staff')

fieldsets=UserAdmin.fieldsets + (
        ("Rôles", {'fields': ('role',)}),  
)
