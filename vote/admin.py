from django.contrib import admin

# Register your models here.
from .models import Item,Voted

class ItemAdmin(admin.ModelAdmin):
    list_display=('title','count')
    list_display_links=['title']
    search_fields=['title']
    list_per_page=25


admin.site.register(Item,ItemAdmin)


class VotedAdmin(admin.ModelAdmin):
    list_display=['username']
    list_display_links=['username']
    search_fields=['username']
    list_per_page=25


admin.site.register(Voted,VotedAdmin)