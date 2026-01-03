from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response

class UserRegistrationAPIView(GenericAPIView):
    permission_classes= (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        # serializer = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        user =serializers.save()
        token=RefreshToken.for_user(user)
        data=serializers.data
        data["tokens"]= {"refresh":str(token),
                         "access":str(token.access_token)}
        
        return Response(status=status.HTTP_201_CREATED)

# workings
# POST /register
#    ↓
# Permission check (AllowAny)
#    ↓
# Serializer validation
#    ↓
# User creation (hashed password)
#    ↓
# JWT token generation
#    ↓
# 201 response + tokens
 

class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = RefreshToken.for_user(user)

        data= serializer.data
        data["tokens"]={"refresh":str(token),
                        "access":str(token.access_token)}

        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    permission_classes= (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refersh_token = request.data["refresh"]
            token = RefreshToken(refersh_token)

            token.blacaklist()
            

            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except Excepption as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

