from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('blog/', include('blog.urls')), # Include the blog app URLs
     path('accounts/', include('django.contrib.auth.urls')), # Include the default auth URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
