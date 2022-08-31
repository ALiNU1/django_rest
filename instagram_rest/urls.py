from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.posts.views import PostViewAPI,PostCreateAPIView,PostUPdateAPIView,PostDeleteAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts', PostViewAPI.as_view(), name="api_posts"),
    path('api/posts/create', PostCreateAPIView.as_view(), name="api_create"),
    path('api/posts/update/<int:pk>', PostUPdateAPIView.as_view(), name="api_update"),
    path('api/posts/delete/<int:pk>', PostDeleteAPIView.as_view(), name="api_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root = settings.MEDIA_ROOT)