from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    filter_horizontal = ()
    ordering = ('email', )
    list_display = ('first_name', 'last_name','email')
    list_filter = ('is_staff', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        (('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),

        (('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'type')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name','last_name', 'email', 'password1', 'password2')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)