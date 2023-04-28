from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from messeges.views import ChatMessageViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('chat',ChatMessageViewSet)

urlpatterns += [
    path('api/', include(router.urls))
]
