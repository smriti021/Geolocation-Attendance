from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # predefined
    path('attendance/', include('attendance.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
    path('', RedirectView.as_view(url='accounts/login/', permanent=False)),  # Redirect root URL to login
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
