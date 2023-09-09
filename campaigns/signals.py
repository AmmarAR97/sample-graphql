from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import EmailCampaign
from .tasks import send_campaign_email
from django.utils import timezone


@receiver(pre_save, sender=EmailCampaign)
def schedule_email_sending(sender, instance, **kwargs):
    now = timezone.now()
    if instance.schedule_time and instance.campaign.is_active:
        try:
            original_instance = sender.objects.select_related('campaign').get(pk=instance.pk)
            if instance.schedule_time != original_instance.schedule_time and instance.schedule_time > now:
                send_campaign_email.apply_async((instance.id,), eta=instance.schedule_time)
        except sender.DoesNotExist:
            pass
