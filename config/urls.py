from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network.views import NetworkNodeViewSet, ContactViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'network', NetworkNodeViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
