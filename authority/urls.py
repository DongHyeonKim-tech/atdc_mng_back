from django.urls import re_path, path
from authority import views

app_name = "authority"

urlpatterns = [
    path('ping/', views.AuthPingView.as_view()),
    path('sign_up/', views.RegisterView.as_view()),
]