from django.db import models


class MusicSchedule(models.Model):
    music = models.FileField(upload_to='./media/music')
    play_from = models.DateTimeField()
    play_up_to = models.DateTimeField()
    sequence = models.IntegerField(default=0)
    last_played_at = models.DateTimeField(null=True, blank=True)