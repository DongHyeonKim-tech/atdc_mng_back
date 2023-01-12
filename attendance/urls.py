from django.urls import re_path, path
from attendance.views import create_acc_recorder_info, create_attd_status_cd, edit_attd_status_cd

app_name = "attendance"

urlpatterns = [
    path('create_acc_recorder_info/', create_acc_recorder_info, name='create_acc_recorder_info'),
    path('create_attd_status_cd/', create_attd_status_cd, name='create_attd_status_cd'),
    path('edit_attd_status_cd/', edit_attd_status_cd, name='edit_attd_status_cd'),
]