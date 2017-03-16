import pyramid_handlers
import Blue_Yellow.infrastructure.static_cache as cache
import Blue_Yellow.controllers.base_controller as base


class HomeController(base.BaseController):

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        # remember what we need to return here is a dictionary
        return {'value': 'HOME'}

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {'value': 'ABOUT'}

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {'value': 'CONTACT'}
