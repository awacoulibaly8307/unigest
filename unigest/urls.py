from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),


    # Authentification (via Djoser)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('',include('unigestAPP.urls')),
    path('api/', include('unigestAPP.api_urls')),
]
