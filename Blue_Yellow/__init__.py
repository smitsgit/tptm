from pyramid.config import Configurator
from Blue_Yellow.controllers import home_controller

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    get_settings(config)

    init_includes(config)
    init_routing(config)
    return config.make_wsgi_app()


def get_settings(config):
    cfg_settings = config.get_settings()
    # db_file = cfg_settings.get('db_file')
    # api_key = cfg_settings.get('api_key')


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_handler('home_ctrl', '/home/{action}', handler=home_controller.HomeController)
    # config.add_route('albums', '/albums')
    # config.add_route('album', '/albums/{name_fragment}')
    # config.add_route('store', '/buy/{name_fragment}')
    config.scan()


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')  # we can call config.addHandler instead of config.addroute
