import Blue_Yellow.infrastructure.static_cache as cache


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = cache.build_cache_id
