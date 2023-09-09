from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='manager_campaign')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.organizer} - {self.title}"

    class Meta:
        indexes = [
            models.Index(fields=['organizer']),
            models.Index(fields=['manager']),
        ]


class EmailCampaign(models.Model):

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    preview_text = models.CharField(max_length=200)
    article_url = models.URLField(null=True, blank=True)
    html_content = models.TextField(null=True, blank=True)
    plain_text_content = models.TextField(null=True, blank=True)
    published_date = models.DateField(blank=True, null=True)
    schedule_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.campaign} - {self.subject}"

    class Meta:
        indexes = [
            models.Index(fields=['campaign']),
            models.Index(fields=['published_date']),
        ]