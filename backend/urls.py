from backend import views
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('applicants/', views.applicant_create),
    re_path(r'^applicants/writing-tasks/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', views.applicant_writing_task),
    re_path(r'^applicants/writing-tasks/files/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', views.file_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)