from Blue_Yellow.viewmodel.base_view_model import BaseViewModel


class RegisterViewModel(BaseViewModel):
    def __init__(self):
        self.email = None
        self.password = None
        self.confirm_password = None
        self.error = None

    def from_dict(self, dict_data):
        self.email = dict_data.get('email')
        self.password = dict_data.get('password')
        self.confirm_password = dict_data.get('confirm_password')
        pass

    def validate(self):
        self.error = None
        if self.password != self.confirm_password:
            self.error = 'The password and confirm password dont match'
            return

        if not self.password:
            self.error = 'Password is empty'
            return

        if not self.email:
            self.error = 'email is empty'
            return
