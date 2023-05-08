from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static


from messeges.views import ChatMessageViewSet
from posts.views import PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('posts/', PostView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('chat',ChatMessageViewSet)

urlpatterns += [
    path('api/', include(router.urls))
]

