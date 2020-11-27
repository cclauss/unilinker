from rest_framework import routers
from main.api import UserViewSet, ProfileViewSet, LinkViewSet

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, 'user')
router.register('api/profile', ProfileViewSet, 'profile')
router.register('api/link', LinkViewSet, 'link')

urlpatterns = router.urls
