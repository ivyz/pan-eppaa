from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Dog,
    )

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(Dog).filter(Dog.name=='Eddy').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'name':one.name, 'project':'paneppaa'}

@view_config(route_name='dogs', renderer='paneppaa:templates/doglist.mako')
def dogs_view(request):
    try:
        dogs = DBSession.query(Dog).order_by('id')
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    return {'dogs':dogs, 'project':'paneppaa'}

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
