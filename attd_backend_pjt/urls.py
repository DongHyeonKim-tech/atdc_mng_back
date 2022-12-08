from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path
from django.urls.conf import include

from rest_framework import routers, permissions

# swagger setting
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title = "Attandance PJT API",
        default_version='v1',
        description='Test description',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('conn_test/', include('conn_test.urls')),
    
    # app path
    path('members/', include('members.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
