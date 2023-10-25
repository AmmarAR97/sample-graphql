from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication


class LoginGraphQLView(GraphQLView):
    authentication_classes = [TokenAuthentication]


# class LogoutGraphQLView(GraphQLView):
#     pass