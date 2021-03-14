from rest_framework.routers import DefaultRouter

from api.views import TaskViewSet

router = DefaultRouter()
router.register(r'notes', TaskViewSet, basename='notes')

urlpatterns = router.urls
