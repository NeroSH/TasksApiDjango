from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from api.views import TaskViewSet

router = DefaultRouter()
router.register(r'notes', TaskViewSet, basename='notes')

urlpatterns = router.urls
