from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from paneppaa.security import groupfinder
from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('dogs', '/dogs')
    config.add_route('dogs_json', '/dogs_json')
    config.add_route('dogdetail', 'dogs/{id}')
    config.add_route('events', '/events')
    config.add_route('events_json', '/events_json')
    config.add_route('eventdetail', 'events/{id}')
    config.add_route('about', '/about')
    config.add_route('advice', '/advice')
    config.add_route('news', '/news')
    config.add_route('addnews', '/editnews')
    config.add_route('editnews', '/editnews')
    config.add_route('help', '/help')
    config.scan()
    # authn_policy = AuthTktAuthenticationPolicy(
    #     'sosecret', callback=groupfinder, hashalg='sha512')
    # authz_policy = ACLAuthorizationPolicy()
    # config = Configurator(settings=settings,
    #                       root_factory='paneppaa.models.RootFactory')
    # config.set_authentication_policy(authn_policy)
    # config.set_authorization_policy(authz_policy)

    return config.make_wsgi_app()
