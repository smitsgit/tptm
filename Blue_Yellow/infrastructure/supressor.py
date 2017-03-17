import pyramid_handlers


class supress(pyramid_handlers.action):

    def __init__(self, _, **kwargs):
        kwargs['request_method'] = 'NOT A HTTP VERB'
        super().__init__(**kwargs)
