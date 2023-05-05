from django.contrib import admin
from django.urls import (
    include,
    path,
)

from mesages.views import (
    MessageViewSet,
)

from rest_framework.routers import DefaultRouter


router = DefaultRouter(
    trailing_slash=False
)

router.register('all-messages', MessageViewSet)

urlpatterns = (
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
)
