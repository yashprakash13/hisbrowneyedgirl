from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import *

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.filter(member = request.user)[0]
        folders = Folder.objects.filter(created_by = request.user)
        
        return render(request, 'profiles/profile.html', {'profile': profile,
                                                        'folders':folders})
