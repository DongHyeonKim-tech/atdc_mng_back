from django.urls import re_path, path
from members.views import (
                            # regist_member, 
                            # create_position_cd, 
                            # create_department_cd, 
                            PositionsView,
                            PositionView,
                            DepartmentsView,
                            DepartmentView
                            )

app_name = "members"

urlpatterns = [
    # path("regist_member/", regist_member, name="regist_member"),
    # path("create_position_cd/", create_position_cd, name="create_position_cd"),
    path("position/", PositionsView.as_view(), name="position"),
    path("position/<int:pk>/", PositionView.as_view(), name="position_detail"),
    path("department/", DepartmentsView.as_view(), name="department"),
    path("department/<int:pk>/", DepartmentView.as_view(), name="department_detail"),
]
