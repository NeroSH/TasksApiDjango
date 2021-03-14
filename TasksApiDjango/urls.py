from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

schema_view = get_schema_view(
    title='Tasks API',
    url='http://127.0.0.1:8000/docs',
    urlconf='api.urls',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('openapi', get_schema_view(
        title="Tasks API",
        description="API to perform GET, POST, PUT methods"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

