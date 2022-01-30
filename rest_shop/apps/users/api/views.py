from rest_framework import generics, serializers
from apps.users.api.serializers import UserDetailSerializer, UserSerializer
from apps.users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)