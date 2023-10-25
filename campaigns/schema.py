from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField
from .models import Campaign, EmailCampaign
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from graphql import GraphQLError
from graphql_jwt.decorators import user_passes_test
from utils.custom_graphql_decorators import custom_user_passes_test


class CampaignType(DjangoObjectType):
    class Meta:
        model = Campaign
        interfaces = (relay.Node,)


class EmailCampaignType(DjangoObjectType):
    class Meta:
        model = EmailCampaign
        interfaces = (relay.Node,)


def is_manager(user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if not default_token_generator.check_token(user, token):
            raise GraphQLError("Token is invalid")
        return user.groups.filter(name='manager').exists()
    except User.DoesNotExist:
        raise GraphQLError("User does not exists")


class Query(ObjectType):
    all_campaigns = DjangoConnectionField(CampaignType)
    all_email_campaigns = DjangoConnectionField(EmailCampaignType)

    @custom_user_passes_test(lambda user: user.groups.filter(name='manager').exists())
    def resolve_all_campaigns(self, info, **kwargs):
        print(info.context.user.id)
        return Campaign.objects.all()

    @user_passes_test(lambda user: user.groups.filter(name='manager').exists())
    def resolve_all_email_campaigns(self, info, **kwargs):
        return EmailCampaign.objects.all()

