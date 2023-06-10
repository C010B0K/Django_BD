from django.contrib import admin

from .models import Text,Photo,Price,Contacts

# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['name','img_preview_list']



admin.site.register(Text)
admin.site.register(Price)
admin.site.register(Contacts)
admin.site.register(Photo, PhotoAdmin)
