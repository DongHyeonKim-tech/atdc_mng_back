from django.urls import re_path, path
from attendance.views import  (
                                AccRecorderInfoView, 
                                AccRecorderInfoDetailView,
                                AttdStatusCdView,
                                AttdStatusCdDetailView,
                                TopAttdStatusCdView,
                                TopAttdStatusCdDetailView
                            )

app_name = "attendance"

urlpatterns = [
    path('recs/', AccRecorderInfoView.as_view(), name='acc_recorder'),
    path('rec/<int:recorder_id>/', AccRecorderInfoDetailView.as_view(), name='acc_recorder'),
    path('attdcds/', AttdStatusCdView.as_view(), name='attd_cd'),
    path('attdcd/<str:attd_cd_id>/', AttdStatusCdDetailView.as_view(), name='attd_cd'),
    path('topcds/', TopAttdStatusCdView.as_view()),
    path('topcd/<str:attd_cd_id>/', TopAttdStatusCdDetailView.as_view()),
]