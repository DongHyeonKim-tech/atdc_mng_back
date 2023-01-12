from django.contrib import admin



# class MemberAdmin(BaseUserAdmin) :
#     list_display = ('mem_id', 'mem_name', 'mem_mail_addr', 'mem_status')
#     list_display_links = ('mem_id',)
#     list_filter = ('mem_id', 'mem_name')
#     search_fields = ('mem_name',)

#     fieldsets = (
#         ("info", {'fields' : ('mem_id', 'mem_name', 'password', 'mem_mail_addr', 'join_dt')}),
#         ("Permissions", {'fields' : ('is_admin', 'auth_cd')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('mem_id', 'mem_name', 'password1', 'password2')
#         }),
#     )

#     filter_horizontal = ()
#     search_fields = ('mem_name',)
#     ordering = ('mem_name',)
    
# admin.site.register(MemberModel, MemberAdmin)
