# Imports
from rest_framework.exceptions import AuthenticationFailed
import jwt
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def validate_token(token):
    if not token:
        raise AuthenticationFailed('UnAuthorized')
    try:
        return jwt.decode(token, env('JWT_SECRET_KEY'), algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token expired')
