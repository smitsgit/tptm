import pyramid_handlers
import Blue_Yellow.infrastructure.static_cache as cache

class HomeController:

    def __init__(self, request):
        self.request = request

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        # remember what we need to return here is a dictionary
        return {'value': 'HOME',
                'build_cache_id': cache.build_cache_id}

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {'value': 'ABOUT',
                'build_cache_id': cache.build_cache_id}

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {'value': 'CONTACT',
                'build_cache_id': cache.build_cache_id}
