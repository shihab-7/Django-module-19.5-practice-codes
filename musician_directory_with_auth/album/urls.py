from django.urls import path
from . import views

urlpatterns = [
     path('add/', views.AlbumCreateView.as_view(), name='album_page'),
    path('edit/<int:pk>/', views.AlbumUpdateView.as_view(), name='edit_album'),
    path('delete/<int:pk>/', views.AlbumDeleteView.as_view(), name='delete_album'),
]
