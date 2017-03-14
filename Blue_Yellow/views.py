from pyramid.view import view_config
from Blue_Yellow.infrastructure import static_cache

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return extend_model({'project': 'Blue_Yellow'})


def extend_model(model_dict):
    model_dict['build_cache_id'] = static_cache.build_cache_id
    return model_dict
