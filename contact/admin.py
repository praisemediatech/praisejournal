from django.contrib import admin

from .models import Contact, ContactInfo, SocialMediaHandles


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']




admin.site.register(SocialMediaHandles)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Contact, ContactAdmin)