from django.contrib import admin
from scheduler.models import MusicSchedule


@admin.register(MusicSchedule)
class MusicScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'music', 'music_url', 'play_from', 'play_up_to', 'sequence', 'last_played_at' ]