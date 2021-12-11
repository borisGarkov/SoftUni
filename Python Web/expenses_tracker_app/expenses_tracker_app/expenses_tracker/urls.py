from django.urls import path

from expenses_tracker_app.expenses_tracker.views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_expenses, name='create'),
    path('edit/<int:pk>', edit_expense, name='edit'),
    path('delete/<int:pk>', delete_expense, name='delete'),
    path('profile/', profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit, name='edit profile'),
    path('profile/delete/', profile_delete, name='delete profile')
]
