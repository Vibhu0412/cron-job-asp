from django.urls import path, include
from rest_framework import routers
from .views import ChallengeStatementViewSet


router = routers.DefaultRouter()
router.register(r'challenge', ChallengeStatementViewSet, basename='challenge')

urlpatterns = [
    path('', include(router.urls)),
]

