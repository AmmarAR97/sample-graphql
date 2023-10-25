from graphene import relay, ObjectType, InputObjectType, Mutation, Field
from graphene import String, Boolean, Int
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField
from .models import Subscriber
from graphql_jwt.decorators import user_passes_test
import re


class SubscriberType(DjangoObjectType):
    class Meta:
        model = Subscriber
        interfaces = (relay.Node,)


class SubscriberInputType(InputObjectType):
    class Meta:
        description = "Input type for creating or updating a subscriber."

    email = String(required=True)
    first_name = String(required=True)
    last_name = String()
    is_active = Boolean()


# email address validation
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(email_regex, email) is not None


class CreateSubscriber(Mutation):
    class Arguments:
        input_data = SubscriberInputType(required=True, description="Input data for creating a subscriber")

    success = Boolean(description="Indicates if the subscriber was successfully created")

    @staticmethod
    def mutate(root, info, input_data):
        email = input_data.get('email')
        if not is_valid_email(email):
            raise ValueError("Invalid email address")
        return CreateSubscriber(success=True)


class UpdateSubscriber(Mutation):
    class Arguments:
        id = Int(required=True)
        data = SubscriberInputType(required=True)

    subscriber = Field(SubscriberType)
    success = Boolean(description="Indicates if the subscriber was successfully created")

    def mutate(self, info, id, data):
        subscriber = Subscriber.objects.get(pk=id)
        for key, value in data.items():
            setattr(subscriber, key, value)
        subscriber.save()
        return UpdateSubscriber(subscriber=subscriber, success=True)


class Query(ObjectType):
    all_subscribers = DjangoConnectionField(SubscriberType)

    @user_passes_test(lambda user: user.groups.filter(name='manager').exists())
    def resolve_all_subscribers(self, info, **kwargs):
        return Subscriber.objects.all()


class Mutation(ObjectType):
    create_subscriber = CreateSubscriber.Field()
    update_subscriber = UpdateSubscriber.Field()
