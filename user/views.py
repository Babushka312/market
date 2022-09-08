
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

from .serializers import MyTokenObtainPairSerializer, UserSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import AnonPermissionOnly


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(APIView):
    permission_classes = (AnonPermissionOnly,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)



