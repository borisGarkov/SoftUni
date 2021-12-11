from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from pythons.pythons_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('all-jobs/', view_all_jobs, name='all jobs')
]
