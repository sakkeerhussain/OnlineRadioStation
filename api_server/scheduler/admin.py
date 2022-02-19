from django.contrib import admin
from scheduler.models import MusicSchedule


@admin.register(MusicSchedule)
class MusicScheduleAdmin(admin.ModelAdmin):
    fields = ['id', 'music', 'play_from', 'play_up_to', 'sequence', 'last_played_at' ]