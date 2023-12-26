from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.MusicianCreateView.as_view(), name='musician'),
    path('edit_musiciian/<int:pk>', views.MusicianUpdateView.as_view(), name='edit_musician'),
    # path('delete_musiciian/<int:pk>', views.MusicianDeleteView.as_view(), name='delete'),
]
