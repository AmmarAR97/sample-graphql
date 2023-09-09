from celery import shared_task
from .models import EmailCampaign
from subscribers.models import Subscriber
from helper.smtp_helper import send_via_smtp


def render_email_template(campaign, subscriber_id):
    base_template = open('campaigns/templates/base_template.html', 'r').read()
    email_content = base_template.replace('{{preview_text}}', campaign.preview_text)
    email_content = email_content.replace('{{article_url}}', campaign.article_url)
    email_content = email_content.replace('{{html_content}}', campaign.html_content)
    email_content = email_content.replace('{{plain_text_content}}', campaign.plain_text_content)
    email_content = email_content.replace('{{published_date}}', campaign.published_date.strftime("%d %b %Y"))

    unsubscribe_url = f'http://127.0.0.1:8000/subscribers/unsubscribe/{subscriber_id}/'
    email_content = email_content.replace('{{unsubscribe_url}}', unsubscribe_url)

    return email_content


@shared_task
def send_campaign_email(email_campaign_id):
    email_campaign = EmailCampaign.objects.get(id=email_campaign_id)
    subscribers = Subscriber.objects.filter(is_active=True)
    for subscriber in subscribers:
        content = render_email_template(email_campaign, subscriber.id)
        # Todo: make to_email dynamic by replacing hardcoded string to --> "subscriber.email"
        message = send_via_smtp(email_campaign.subject, "ammar.abdur.1@gmail.com", content)
        if message:
            print(f"Sent mail successfully to {subscriber.email}")
        else:
            print(f"Failed to send mail to {subscriber.email}")
