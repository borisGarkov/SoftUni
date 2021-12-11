from django.urls import path

from notes.notes_app.views import home, add_note, edit, delete_note, details, profile, delete_profile

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details, name='details'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
