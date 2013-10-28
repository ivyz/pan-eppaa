from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Dog,
    Event,
    News
    )


#DOGS
@view_config(route_name='home', renderer='paneppaa:templates/doglist.mako')
def home_view(request):
    try:
        dogs = DBSession.query(Dog).order_by('id')
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    return {'dogs':dogs, 'project':'paneppaa'}


@view_config(route_name='dogs', renderer='paneppaa:templates/doglist.mako')
def dogs_view(request):
    try:
        dogs = DBSession.query(Dog).order_by('id')
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    return {'dogs':dogs, 'project':'paneppaa'}


@view_config(route_name='dogdetail', renderer='paneppaa:templates/dogdetail.mako')
def dog_view(request):
    try:
        dog = DBSession.query(Dog).filter(Dog.id==request.matchdict['id']).first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    return {'dog':dog, 'project':'paneppaa'}


@view_config(route_name='dogs_json', renderer='json')
def dogs_json(request):
    try:
        dogs = DBSession.query(Dog).order_by('id')
    except DBAPIError:
        return dict(success=False, message="Errore")

    result = []
    for d in dogs:
        plaindog = {}
        plaindog['name'] = d.name
        plaindog['description']= d.description
        plaindog['born_year'] = d.born_year
        plaindog['size'] = d.size
        plaindog['kind'] = d.kind
        plaindog['image'] = d.image
        result.append(plaindog)

    return {'dogs': result}


#EVENTS
@view_config(route_name='events', renderer='paneppaa:templates/eventlist.mako')
def events_view(request):
    try:
        events = DBSession.query(Event).order_by('id')
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    return {'events':events, 'project':'paneppaa'}


@view_config(route_name='events_json', renderer='json')
def eventss_json(request):
    try:
        events = DBSession.query(Event).order_by('id')
    except DBAPIError:
        return dict(success=False, message="Errore")

    result = []
    for d in events:
        plainevent = {}
        plainevent['title'] = d.title
        plainevent['description']= d.description
        plainevent['date'] = str(d.date)
        plainevent['image'] = d.image
        result.append(plainevent)

    return {'events': result}

@view_config(route_name='eventdetail', renderer='paneppaa:templates/eventdetail.mako')
def event_view(request):
    try:
        event = DBSession.query(Event).filter(Event.id==request.matchdict['id']).first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    return {'event':event}


#ABOUT
@view_config(route_name='about', renderer='paneppaa:templates/about.mako')
def about_view(request):
    return {'project':'paneppaa'}


#NEWS
@view_config(route_name='news', renderer='paneppaa:templates/news.mako')
def news_view(request):
    try:
       news = DBSession.query(News).order_by('id')
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

        return {'news': news, 'project':'paneppaa'}

@view_config(route_name='editnews', renderer='paneppaa:templates/editnews.mako', permission='edit')
def editnews_view(request):
    try:
        news = DBSession.query(News).filter(News.id==request.matchdict['id']).first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

        return {'news': news, 'project':'paneppaa'}


#HELP
@view_config(route_name='help', renderer='paneppaa:templates/help.mako')
def help_view(request):
    return {'project':'paneppaa'}


#ADVICE
@view_config(route_name='advice', renderer='paneppaa:templates/advice.mako')
def advice_view(request):
    return {'project':'paneppaa'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_paneppaa_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
