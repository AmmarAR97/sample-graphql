from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-id',)

admin.site.register(Subscriber, SubscriberAdmin)

