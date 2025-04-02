from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        ("User Details", {'fields': ('email', 'password1', 'password2')}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_admin')}),
    )
