from rest_framework import viewsets, permissions
from main.serializers import UserSerializer
from main.models import Profile
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
