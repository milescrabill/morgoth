from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from morgoth.base import views
from morgoth.base.api.views import UserViewSet

# API Router
router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'', views.index, name='index'),
]
