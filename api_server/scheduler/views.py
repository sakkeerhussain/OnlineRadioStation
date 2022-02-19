from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.views import generic

from scheduler.models import MusicSchedule


class NextMusicView(generic.View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        music_schedule = MusicSchedule.objects \
            .filter(Q(music__isnull=False) | Q(music_url__isnull=False)) \
            .filter(play_from__lte=now, play_up_to__gte=now) \
            .order_by('last_played_at', 'sequence') \
            .first()

        music_schedule.last_played_at = now
        music_schedule.save()

        return HttpResponse(music_schedule.get_music_url(request))
