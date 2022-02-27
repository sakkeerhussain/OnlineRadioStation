from django.contrib import admin
from scheduler.models import MusicSchedule


@admin.register(MusicSchedule)
class MusicScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_music', 'play_from', 'play_up_to', 'sequence', 'last_played_at', 'is_repeat']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.request = None

    def queryset(self, request):
        qs = super(MusicScheduleAdmin, self).queryset(request)
        self.request = request
        return qs

    def get_music(self, obj):
        return obj.get_music_url(self.request)

    get_music.short_description = 'Music'
