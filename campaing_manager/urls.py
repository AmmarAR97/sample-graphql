from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from .schema import schema
from .views import LoginGraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscribers/', include('subscribers.urls')),
    path("graphql/", csrf_exempt(LoginGraphQLView.as_view(graphiql=True, schema=schema)))
]
