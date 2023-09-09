from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} - {self.email}"
