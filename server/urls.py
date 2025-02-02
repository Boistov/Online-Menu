from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
