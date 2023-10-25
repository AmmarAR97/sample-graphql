from rest_framework import generics
from .models import Subscriber
from .serializers import SubscriberSerializer
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse


class SubscriberView(generics.CreateAPIView):
    """
    This view is used to add a new entry to Subscriber model
    use POST method with the following sample data:
    {
        "email": "ammar@gmail.co",
        "first_name": "AMMAR",
        "is_active": true
    }
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class ReSubscribeView(generics.RetrieveAPIView):
    """
    This view is used to set inactive subscriber to active
    using GET method since a clickable link is provided in the email.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = True
        instance.save()

        template = loader.get_template('subscribed_successfully.html')
        html_content = template.render()

        return HttpResponse(html_content, content_type='text/html')


class UnSubscribeView(generics.RetrieveUpdateAPIView):
    """
    This view is used to set subscriber is_active = False
    using GET method since a clickable link is provided in the email.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        template = loader.get_template('unsubscribed_template.html')

        resubscribe_url = request.build_absolute_uri(reverse('resubscribe', kwargs={'pk': kwargs['pk']}))
        context = {
            'resubscribe_url': resubscribe_url
        }
        html_content = template.render(context)

        return HttpResponse(html_content, content_type='text/html')


from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

class HasuraWebhookView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    # serializer_class = SubscriberSerializer

    def get(self, request, *args, **kwargs):
        auth_token = request.META.get('HTTP_AUTHORIZATION', '').replace('Token ', '')
        table = request.META.get('HTTP_Table')
        if auth_token != "":
            try:
                token = Token.objects.get(key=auth_token)
                user_id = token.user.id
                user = User.objects.get(id=user_id)
                user_groups = user.groups.all()
                # group_names = list(user_groups.values_list('name', flat=True))
                response_data = {
                    "X-Hasura-User-Id": str(user_id),
                    "x-hasura-default-role": "user",
                    "x-hasura-role": "user",
                    # "x-hasura-allowed-roles": str(group_names),
                }
                return JsonResponse(response_data)
            except Token.DoesNotExist:
                # If the token does not exist, return a 401 Unauthorized response
                return HttpResponse(status=401)
        else:
            return HttpResponse(status=401)


