from django.urls import re_path, path
from members.views import (
                            regist_member, 
                            # create_position_cd, 
                            create_department_cd, 
                            PositionView)

app_name = "members"

urlpatterns = [
    path("regist_member/", regist_member, name="regist_member"),
    # path("create_position_cd/", create_position_cd, name="create_position_cd"),
    path("position/", PositionView.as_view(), name="position_cd"),
    path("create_department_cd/", create_department_cd, name="create_department_cd"),
]
