from django.urls import path 
from apps.users.views import UserAPIView ,RegisterView


urlpatterns = [
    path('api/users', UserAPIView.as_view(), name = "api_users"),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
] 