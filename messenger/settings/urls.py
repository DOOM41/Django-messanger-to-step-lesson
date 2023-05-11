from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from messeges.views import ChatMessageViewSet
from auths.views import VerifyView


def trigger_error(request):
    division_by_zero = 1 / 0 # noqa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('sentry-debug/', trigger_error),
    path('api/verificate', VerifyView.as_view()),
]

router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)

router.register('chat',ChatMessageViewSet)

urlpatterns += [
    path('api/', include(router.urls))
]
