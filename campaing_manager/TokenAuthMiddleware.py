from rest_framework.authtoken.models import Token
from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import AuthenticationFailed
import django.middleware.common
from rest_framework import HTTP_HEADER_ENCODING, exceptions


class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            auth = TokenAuthentication()
            user, _ = auth.authenticate(request)
            request.user = user if user else AnonymousUser()
        except Exception as E:
            pass

        response = self.get_response(request)
        return response

