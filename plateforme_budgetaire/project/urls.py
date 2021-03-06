from django.conf.urls import patterns, url
from project.views import *

urlpatterns = patterns(
    '',
    url(r'^view/(?P<pk>\d+)$', ProjectDetail.as_view(), name='project_detail'),
    url(r'^(?P<validated>0|1|2)$', ProjectList.as_view(), name='project_list'),
    url(r'^create/$', ProjectCreate.as_view(), name='project_create'),
    url(r'^list/$', ProjectList.as_view(), {"validated": "all"}, name='project_list'),

    # Function
    url(r'^accept/(\d+)$', accept_project, name="project_accept"),
    url(r'^refuse/(\d+)$', refuse_project, name="project_refuse"),
)
