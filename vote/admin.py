from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display=('title','count')
    list_display_links=['title']
    search_fields=['title']
    list_per_page=25


admin.site.register(Item,ItemAdmin)

class UserprofileInline(admin.StackedInline):
    model=Userprofile
    can_delete=False
    verbose_name_plural='User'

class UserAdmin(BaseUserAdmin):
    inlines=(UserprofileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)