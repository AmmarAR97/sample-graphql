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

