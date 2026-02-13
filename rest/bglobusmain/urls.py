from django.contrib import admin
from django.urls import path, include
from app.categories.urls import router
from app.product.urls import router as product_router
from app.utilities.urls import router as document_router
from app.services.urls import router as service_router
from app.news.urls import router as news_router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(product_router.urls)),
    path('api/v1/', include(document_router.urls)),
    path('api/v1/', include(service_router.urls)),
    path('api/v1/', include(news_router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)