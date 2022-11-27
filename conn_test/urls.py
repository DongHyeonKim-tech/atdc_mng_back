from django.urls import re_path, path
from conn_test.views import connection_test

app_name = "connection_test"

urlpatterns = [
    path('call/', connection_test, name='connection_test'),
]
