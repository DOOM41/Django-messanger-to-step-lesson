import redis
import json
from django.http import HttpRequest
from rest_framework.response import Response
import functools


r = redis.Redis(host='localhost', port=6379, db=0)


def cache_in_redis(key: str, timeout: int):
    """
    Декоратор кеширования результатов запроса в Redis.
    """
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            response = r.get(key)
            if response:
                response = json.loads(response)
                return Response(response, status=200)

            response = view_func(request, *args, **kwargs)

            if isinstance(response, Response) and \
                isinstance(response.data, (list, dict)):
                r.set(key, json.dumps(response.data), ex=timeout)

            return response

        return wrapper

    return decorator