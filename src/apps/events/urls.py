from rest_framework.routers import DefaultRouter

from .viewsets import EventViewSet

router = DefaultRouter()
router.register("events", EventViewSet, basename="events")

urlpatterns = [] + router.urls
