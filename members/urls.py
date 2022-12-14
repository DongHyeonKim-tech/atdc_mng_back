from django.urls import re_path, path
from members import views

app_name = "members"

urlpatterns = [
    path('/', views.RegisterView.as_view()),
    path('ping/', views.AuthPingView.as_view()),
    
]
