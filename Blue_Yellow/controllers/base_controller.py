import Blue_Yellow.infrastructure.static_cache as cache
import pyramid.renderers


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = cache.build_cache_id

        layout_renderer = pyramid.renderers.get_renderer('Blue_Yellow:templates/shared/_layout.pt')
        impl = layout_renderer.implementation()
        self.common_layout = impl['common_layout']
        # self.additional_css = impl['additional_css']
        # self.additional_js = impl['additional_js']

    @property
    def is_logged_in(self):
        return False
