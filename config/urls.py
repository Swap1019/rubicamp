from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rubikamp/', include('rubikamp.urls')),
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static-like assets from templates/generated-website/
urlpatterns += [
    re_path(
        r'^new-shop/(?P<path>.*\.(css|js|png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot|ico))$',
        serve,
        {'document_root': os.path.join(settings.BASE_DIR, 'templates', 'generated-website')}
    ),
]
