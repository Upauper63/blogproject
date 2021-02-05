from django.contrib import admin
from django.urls import path, include
import os
# dev
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path(os.environ.get('ADMIN_URL') + '/', admin.site.urls),
    path('', include('blog.urls')),
]

# dev
#  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)