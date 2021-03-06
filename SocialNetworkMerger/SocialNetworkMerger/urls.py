from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import login_redirect

urlpatterns = [
    path('', login_redirect, name='login_redirect'),
    path('home/', include('home.urls', namespace='home')),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('medialook/', include('foreignapi.urls', namespace='foreignapi'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
