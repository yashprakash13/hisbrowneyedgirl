from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.ProfileView.as_view(), name="profile"),
    path('folder/<int:folder_id>/', views.FolderDetailView.as_view(), name='folder_detail'),
]