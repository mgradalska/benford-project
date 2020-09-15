from rest_framework import routers
from benford_analyzer.views import BenfordAnalyzerView
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r"datasets", BenfordAnalyzerView, basename="benford analyzer")

urlpatterns = [
    url(r"api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
