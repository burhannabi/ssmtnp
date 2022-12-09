from django.urls import path, include
from .views import *

urlpatterns = [
    path('resume/<int:id>', UserResume.as_view(),name='del-resume'),
    path('resume', UserResume.as_view(),name='add-resume'),
    path('all/jobs', AllJobs.as_view(),name='all_jobs'),
    path('all/jobs/<int:id>', ApplyJob.as_view(),name='apply_jobs'),
    path('student/job', StudentJob.as_view(),name='student_job'),
    path('chat', Chat.as_view(),name='chat'),
    path('chat/<int:id>', ChatUser.as_view(),name='chat_user'),
    path('placement', PlacementTraning.as_view(),name='placement'),
    path('placement/<int:id>', TraningInfo.as_view(),name='placement_info'),
]
