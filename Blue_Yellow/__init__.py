from pyramid.config import Configurator
import os
import Blue_Yellow
from Blue_Yellow.controllers import home_controller
from Blue_Yellow.controllers  import albums_controller
from Blue_Yellow.controllers  import account_controller
from Blue_Yellow.data.dbsession import DbSessionFactory


def init_db(config):
    top_dir = os.path.dirname(Blue_Yellow.__file__)
    rel_path = os.path.join('db', 'blue_yellow.sqlite')
    db_file = os.path.join(top_dir, rel_path)
    DbSessionFactory.global_init_database(db_file)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    get_settings(config)

    init_includes(config)
    init_routing(config)
    init_db(config)
    return config.make_wsgi_app()


def get_settings(config):
    cfg_settings = config.get_settings()
    # db_file = cfg_settings.get('db_file')
    # api_key = cfg_settings.get('api_key')


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_handler('root', '/', handler=home_controller.HomeController, action='index')
    add_controller_routes(config, home_controller.HomeController, 'home')
    add_controller_routes(config, albums_controller.AlbumController, 'albums')
    add_controller_routes(config, account_controller.AccountController, 'account')
    config.scan()


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')  # we can call config.addHandler instead of config.addroute


def add_controller_routes(config, ctrl, prefix):
    print('adding route {}'.format('/' + prefix))
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    print('adding route {}'.format('/' + prefix + '/'))
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    print('adding route {}'.format('/' + prefix + '/{action}'))
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    print('adding route {}'.format('/' + prefix + '/{action}/'))
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    print('adding route {}'.format('/' + prefix + '/{action}/{id}'))
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl)
