from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('', include('user.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
