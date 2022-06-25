# Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, UserLinksSerializer
from .models import User, UserLinks
from .utils.helpers import validate_token

import jwt
import datetime
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


# Views
class RegisterView(APIView):
    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class LoginView(APIView):

    @staticmethod
    def post(request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Invalid credentials')

        payload = {
            'id': user.id,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, env('JWT_SECRET_KEY'), algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'ok': True,
            'message': 'Login successful',
            'data': {
                'id': user.id,
                'email': user.email
            }
        }

        return response


class UserView(APIView):

    @staticmethod
    def get(request):
        payload = validate_token(request.COOKIES.get('jwt'))
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogOutView(APIView):
    @staticmethod
    def get(request):
        response = Response()

        response.set_cookie(key='jwt', value='', httponly=True)

        response.data = {
            'ok': True,
            'message': 'Logout successful'
        }

        return response


class AddLinkView(APIView):

    @staticmethod
    def post(request):
        payload = validate_token(request.COOKIES.get('jwt'))
        request.data['user_id'] = payload['id']
        serializer = UserLinksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GetLinksView(APIView):

    @staticmethod
    def get(request):
        links = UserLinks.objects.filter(user_id=request.GET['user_id'])
        serializer = UserLinksSerializer(links, many=True)
        return Response(serializer.data)


class UpdateLinksView(APIView):

    @staticmethod
    def put(request):
        payload = validate_token(request.COOKIES.get('jwt'))

        user_link = UserLinks.objects.get(id=request.GET['id'])
        request.data['user_id'] = payload['id']
        serializer = UserLinksSerializer(instance=user_link, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
