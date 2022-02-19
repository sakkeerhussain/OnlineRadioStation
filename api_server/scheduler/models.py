from django.db import models


class MusicSchedule(models.Model):
    music = models.FileField(upload_to='./media/music', null=True, blank=True)
    music_url = models.CharField(max_length=500, null=True, blank=True)
    play_from = models.DateTimeField()
    play_up_to = models.DateTimeField()
    sequence = models.IntegerField(default=0)
    last_played_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.music.url if self.music else self.music_url

    def get_music_url(self, request):
        return request.build_absolute_uri(self.music.url) if self.music else self.music_url
