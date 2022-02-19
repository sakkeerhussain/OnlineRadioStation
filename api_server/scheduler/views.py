from django.http import HttpResponse
from django.views import generic


class NextMusicView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('https://dns2.vippendu.com/128k/546276/32408561/Kannamma--From-Veyil--Pradeep-Kumar.mp3')