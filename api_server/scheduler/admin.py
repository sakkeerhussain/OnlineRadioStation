from django.contrib import admin
from scheduler.models import MusicSchedule


@admin.register(MusicSchedule)
class MusicScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_music', 'play_from', 'play_up_to', 'sequence', 'last_played_at', 'is_repeat']

    def get_music(self, obj):
        return str(obj)

    get_music.short_description = 'Music'
