from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


# from . import models

class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        data = {
            "message": "Logout"
        }
        return Response(data=data, status=status.HTTP_200_OK)


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['Response'] = 'Registration Successfully'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
