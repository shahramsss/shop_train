from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .froms import UserChangeForm, UserCreationForm
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'full_name', 'phone' , 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'phone' ,'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'full_name', 'phone' , 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
