from django.contrib.auth import get_user_model

from rest_framework import status, viewsets
from rest_framework .decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# from .renderers import UserJSONRenderer
from .serializers import UserRegistrationSerializer, UserLoginSerializer

User = get_user_model()


class UserAPIView(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)

    @action(['post'], detail=False)
    def registration(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(['post'], detail=False)
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
