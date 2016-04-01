from django.conf.urls import patterns, url
from vote.views import *

urlpatterns = patterns(
    '',
    url(r'^formulaire/$', formulaire, name='formulaire'),
)
