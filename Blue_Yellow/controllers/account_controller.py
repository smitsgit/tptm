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
        return {
            'email': None,
            'password': None,
            'confirm_password': None,
            'error': None
        }

    # POST - account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        confirm_password = self.request.POST.get('confirm_password')
        print("Email {} Password {} - Confirm {}".format(email, password, confirm_password))

        if password != confirm_password:
            return {
                'email': email,
                'password': password,
                'confirm_password': confirm_password,
                'error': 'The password and confirm password dont match'
            }

        # verify if the account already exists and password match
        # Create new account in DB
        # send welcome email

        # redirect - In Pyramid if you wish to redirect , just raise a particular type of exception
        self.redirect('/account')
        return {}
