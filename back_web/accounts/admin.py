from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, CustomGroup

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # displayed as user table in admin console
    list_display = ('username', 'email', 'is_active',
        'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('custom_group', 'is_active', 'is_staff', 'is_superuser')
    # show items in details
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'custom_group',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
            'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('custom_group', 'email',)
    ordering = ('custom_group', 'email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup)

