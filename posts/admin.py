from django.contrib import admin
from models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    ordering = ['creation_date']

admin.site.register(Announcement, AnnouncementAdmin)
