from django.contrib import admin
from authority.models import User as UserModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin) :
    list_display = ('user_id', 'auth_cd', 'user_status')
    list_display_links = ('user_id',)
    list_filter = ('user_id',)
    search_fields = ('user_id',)

    fieldsets = (
        ("info", {'fields' : ('user_id', 'password', 'create_dt', 'modify_dt')}),
        ("Permissions", {'fields' : ('is_admin', 'auth_cd')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'password1', 'password2')
        }),
    )

    filter_horizontal = ()
    search_fields = ('user_id',)
    ordering = ('user_id',)
    
admin.site.register(UserModel, UserAdmin)