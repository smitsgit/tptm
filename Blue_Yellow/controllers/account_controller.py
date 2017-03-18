import pyramid_handlers

import Blue_Yellow.controllers.base_controller as base


class AccountController(base.BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt')
    def signin(self):
        return {}

    # GET - account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='GET',
                             name='register')
    def register_get(self):
        return {}

    # POST - account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        return {}
