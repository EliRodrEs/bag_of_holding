from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('', include('user.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

    re_path(r'^rosetta/', include('rosetta.urls'))
]
