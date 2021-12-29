from django.urls import path
from django.views.generic import TemplateView

from mvtapp.views import detail

app_name = 'mvtapp'

urlpatterns = [
    path('detail/', detail, name='detail'),
    path('meetings/', TemplateView.as_view(template_name='reg_meeting.html'), name='meetings'),  #회의만들기 페이지 이동
    path('meetings_list/', TemplateView.as_view(template_name='meeting_log_list.html'), name='meetings_list'),  #회의만들기 페이지 이동
    path('voice_meeting/', TemplateView.as_view(template_name='voice_meeting.html'), name='voice_meeting')  #
]