import pyramid_handlers

import Blue_Yellow.controllers.base_controller as base
from Blue_Yellow.viewmodel.register_view_model import RegisterViewModel


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
        vm = RegisterViewModel()
        return vm.to_dict()

    # POST - account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)
        print("Email {} Password {} - Confirm {}".format(vm.email, vm.password, vm.confirm_password))

        vm.validate()
        if vm.error:
            return vm.to_dict()

        # verify if the account already exists and password match
        # Create new account in DB
        # send welcome email

        # redirect - In Pyramid if you wish to redirect , just raise a particular type of exception
        self.redirect('/account')
        return {}
