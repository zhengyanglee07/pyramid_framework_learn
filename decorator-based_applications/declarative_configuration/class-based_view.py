from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response


class ClassBasedView(object) :
    def __init__(self, request) :
         self.request = request

    @view_config(route_name='first_view')
    def first_view(request) :
        return Response('First View')
    
    @view_config(route_name='second_view')
    def second_view(request) :
        return Response('Second View')


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route('first_view', '/1')
        config.add_route('second_view', '/2')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('202.75.56.8', 80, app)  # Server configuration
    # server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
