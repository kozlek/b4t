from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

LATEST_VERSION = "v1"

api_urlpatterns = [
    path("", include("src.apps.appointment.urls")),
    path("", include("src.apps.user.urls")),
    path("", include("src.apps.events.urls")),
]

urlpatterns = [
    path("", RedirectView.as_view(url=f"/api/{LATEST_VERSION}/")),
    path(
        f"api/{LATEST_VERSION}/",
        include((api_urlpatterns, "api"), namespace=LATEST_VERSION),
    ),
    path("admin/", admin.site.urls),
]
