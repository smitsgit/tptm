from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    cfg_settings = config.get_settings()
    # db_file = cfg_settings.get('db_file')
    # api_key = cfg_settings.get('api_key')
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')  # we can call config.addHandler instead of config.addroute

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('albums', '/albums')
    config.add_route('album', '/albums/{name_fragment}')
    config.add_route('store', '/buy/{name_fragment}')
    config.scan()
    return config.make_wsgi_app()
