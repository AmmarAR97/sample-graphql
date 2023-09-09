from django.contrib import admin
from .models import Campaign
from .models import EmailCampaign

admin.site.register(Campaign)
admin.site.register(EmailCampaign)
