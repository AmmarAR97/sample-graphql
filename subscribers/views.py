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

