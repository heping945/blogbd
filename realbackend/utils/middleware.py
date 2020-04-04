from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django_redis import get_redis_connection

from utils.func import IpRecord
iplog = get_redis_connection('ip')



# logger = logging.getLogger('django')


class RefuseRequests(MiddlewareMixin):
    def process_request(self, request):
        http_user_agent = request.META.get('HTTP_USER_AGENT', '')
        if http_user_agent and 'requests' in http_user_agent:
            d = {'err': '权限出错'}
            return JsonResponse(d, )
        return None


class SetRemoteAddrFromForwardedFor(MiddlewareMixin):
    def process_request(self, request):
        instance = IpRecord(iplog)
        ip = request.META.get('HTTP_X_REAL_IP', '')
        if ip:
            instance.set(ip)
