from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.shop.urls')),
    path('authenticate/', include('apps.authenticate.urls')),
    path('shopping/', include('apps.shopping_cart.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
