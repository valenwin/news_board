from django.urls import path, include
from rest_framework import routers

from .views import BaseTemplateView
from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', BaseTemplateView.as_view()),
    path('api/', include(router.urls)),

]
