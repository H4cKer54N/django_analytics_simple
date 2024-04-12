from .models import Analytics
from django.contrib import admin

class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('browser', 'os', 'device', 'url', 'ip_address', 'country', 'city', 'created_at', 'referer')
    search_fields = ('browser', 'os', 'device', 'url', 'ip_address', 'country', 'city', 'referer')
    list_filter = ('browser', 'os', 'device', 'country', 'city')

admin.site.register(Analytics, AnalyticsAdmin)