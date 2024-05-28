
# to secure connection
import re
from django.conf import settings

class DynamicNgrokCsrfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]
        ngrok_pattern = re.compile(r'.*\.ngrok-free\.app$')
        if ngrok_pattern.match(host) and f"https://{host}" not in settings.CSRF_TRUSTED_ORIGINS:
            settings.CSRF_TRUSTED_ORIGINS.append(f"https://{host}")
        return self.get_response(request)
