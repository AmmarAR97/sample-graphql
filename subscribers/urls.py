from django.urls import path
from .views import SubscriberView, ReSubscribeView, UnSubscribeView, HasuraWebhookView


urlpatterns = [
    path('subscribe/', SubscriberView.as_view(), name='subscription'),
    path('resubscribe/<int:pk>/', ReSubscribeView.as_view(), name='resubscribe'),
    path('unsubscribe/<int:pk>/', UnSubscribeView.as_view(), name='unsubscribe'),
    path('webhook/auth/', HasuraWebhookView.as_view(), name='HasuraWebhookView'),
]

