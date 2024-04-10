from django.db import models

class Analytics(models.Model):
    browser = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    referer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ip_address