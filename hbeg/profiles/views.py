from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import *

class ProfileView(LoginRequiredMixin, View):
    """View to display profile page
    """
    def get(self, request):
        profile = Profile.objects.filter(member = request.user)[0]
        folders = Folder.objects.filter(created_by = request.user)
        context = {
            'profile': profile,
            'folders':folders
                    }

        return render(request, 'profiles/profile.html', context)


class FolderDetailView(LoginRequiredMixin, View):
    """View to show detail view of a folder
    """
    def get(self, request, folder_id):
        folder = Folder.objects.get(pk=folder_id)
        context = {
            'folder' : folder
        }

        return render(request, 'profiles/folder_detail.html', context)