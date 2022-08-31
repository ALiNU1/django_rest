from django.urls import path 
from apps.users.views import UserAPIView


urlpatterns = [
    path('api/users', UserAPIView.as_view(), name = "api_users"),
] 