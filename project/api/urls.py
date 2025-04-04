from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from .article.views import ArticleViewSet
from .user.views import UserAPIView


router = routers.DefaultRouter()
router.register('article', ArticleViewSet, 'article')
router.register('user', UserAPIView, 'user')

schema_view = get_schema_view(
    openapi.Info(
        title='MYSITE BACKEND API',
        default_version='v1',
        description='Routes of MYSITE BACKEND',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger(<str:format>.json|.yaml)/', schema_view.without_ui(), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('', include((router.urls, 'api-root')), name='api-root'),
    # path('celery/result/<pk>/', CeleryResultView.as_view()),
]
