from django.urls import include, path
from rest_framework.routers import DefaultRouter
from titles.views import CategoryViewSet, GenreViewSet, TitlesViewSet

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='Category')
router_v1.register('genres', GenreViewSet, basename='Genre')
router_v1.register('titles', TitlesViewSet, basename='Title')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
