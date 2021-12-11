from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('todos/', views.show_todos, name='show todos')
]
