import Blue_Yellow.infrastructure.static_cache as cache
import pyramid.renderers
import pyramid.httpexceptions as exc


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = cache.build_cache_id

        layout_renderer = pyramid.renderers.get_renderer('Blue_Yellow:templates/shared/_layout.pt')
        impl = layout_renderer.implementation()
        self.common_layout = impl['common_layout']


    @property
    def is_logged_in(self):
        return False

    def redirect(self, url_to, permanent=False):
        if permanent:
           raise exc.HTTPMovedPermanently(url_to)
        raise exc.HTTPFound(url_to)
