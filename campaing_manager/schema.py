


# from graphene import InputObjectType, Mutation

from subscribers.models import Subscriber
from graphql import GraphQLError
# from django.contrib.auth.models import .
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
# from django.contrib.auth.decorators import user_passes_test
import graphql_jwt
from django.contrib.auth.models import User as user
from campaigns.schema import Query as CampaignsQuery
from subscribers.schema import Query as SubscribersQuery
from subscribers.schema import Mutation as SubscribersMutation


import graphene
import graphql_jwt


# We must define a query for our schema
class Query(CampaignsQuery, SubscribersQuery, graphene.ObjectType):
    pass


class Mutation(SubscribersMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)





#
#
# class CampaignInputType(InputObjectType):
#     title = graphene.String(required=True)
#     description = graphene.String()
#     start_date = graphene.Date()
#     end_date = graphene.Date()
#     budget = graphene.Float()
#     organizer_id = graphene.Int()
#     manager_id = graphene.Int()
#     is_active = graphene.Boolean()
#
# class EmailCampaignInputType(InputObjectType):
#     campaign_id = graphene.Int(required=True)
#     subject = graphene.String(required=True)
#     preview_text = graphene.String()
#     article_url = graphene.String()
#     html_content = graphene.String()
#     plain_text_content = graphene.String()
#     published_date = graphene.Date()
#     schedule_time = graphene.DateTime()
#
#

#
#

#
#
# class DeleteSubscriber(Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#
#     success = graphene.Boolean()
#
#     def mutate(self, info, id):
#         try:
#             subscriber = Subscriber.objects.get(pk=id)
#             subscriber.delete()
#             return DeleteSubscriber(success=True)
#         except Subscriber.DoesNotExist:
#             return DeleteSubscriber(success=False)
#
#
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from django.http import JsonResponse
#
# # @permission_classes([IsManager])

#
#
# class Mutation(graphene.ObjectType):
#     create_subscriber = CreateSubscriber.Field()
#     update_subscriber = UpdateSubscriber.Field()
#     delete_subscriber = DeleteSubscriber.Field()
#
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()
#
#
#
# schema = graphene.Schema(query=Query, mutation=Mutation)

