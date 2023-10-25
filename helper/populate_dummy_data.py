from campaigns.models import Campaign, EmailCampaign
from subscribers.models import Subscriber
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


def populate_subscribers():
    failed_count = 0
    for _ in range(10000):
        try:
            Subscriber.objects.create(
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                is_active=fake.boolean(chance_of_getting_true=80)
            )
        except Exception as E:
            failed_count += 1
            print("\n",E)
            print(f"failed_count = {failed_count}")


def populate_campaigns():
    for _ in range(10000):
        campaign_failed_count = 0
        try:
            campaign = Campaign.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                start_date=fake.date_between(start_date='-30d', end_date='today'),
                end_date=fake.date_between(start_date='today', end_date='+30d'),
                budget=random.randint(1000, 5000),
                organizer=None,
                manager=None,
                is_active=fake.boolean(chance_of_getting_true=80)
            )
        except Exception as E:
            campaign_failed_count += 1
            print("\n", E)
            print(f"campaign_failed_count = {campaign_failed_count}")
        # Create 3 email campaigns for each campaign
        email_failed_count = 0
        for _ in range(100):
            try:
                EmailCampaign.objects.create(
                    campaign=campaign,
                    subject=fake.sentence(),
                    preview_text=fake.sentence(),
                    article_url=fake.url(),
                    html_content=None,
                    plain_text_content=fake.paragraph(),
                    published_date=datetime.now() - timedelta(days=random.randint(1, 30))
                )
            except Exception as E:
                email_failed_count += 1
                print("\n", E)
                print(f"email_failed_count = {email_failed_count}")
