from django.contrib.auth.models import User
from rest_framework import viewsets

from api.serializers.UserSerializer import UserSerializer


class UserViewAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
