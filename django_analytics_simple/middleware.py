import os
from django.utils.deprecation import MiddlewareMixin
import maxminddb
from .models import Analytics
from user_agents import parse
from django.conf import settings

class AnalyticsMiddleware(MiddlewareMixin):

    def obtener_informacion_de_ip(self,ip_address):
        mmdb_path = os.path.join(os.path.dirname(__file__), 'data', 'GeoLite2-City.mmdb')
        with maxminddb.open_database(mmdb_path) as mmdb:
            return mmdb.get(ip_address)
    
    def process_request(self, request):
        user_agent_string = request.META.get('HTTP_USER_AGENT', '')
        user_agent = parse(user_agent_string)
        browser = user_agent.browser.family
        os = user_agent.os.family
        device = user_agent.device.family
        url = request.path
        referer = request.META.get('HTTP_REFERER', '')
        ip_address = request.META.get('REMOTE_ADDR', '')
        location_info = self.obtener_informacion_de_ip(ip_address)
        if location_info:
            print(location_info)
            lang_code = settings.ANALYTICS_LANGUAGE
            city = location_info.get('city', {}).get('names', {}).get(lang_code, 'en')
            country = location_info.get('country', {}).get('names', {}).get(lang_code, 'en')
        else:
            city = ''
            country = ''
        Analytics.objects.create(
            browser=browser,
            os=os,
            device=device,
            url=url,
            city=city,
            country=country,
            ip_address=ip_address,
            referer=referer
        )
        return None
    