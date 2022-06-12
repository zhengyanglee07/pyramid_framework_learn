from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('');
    # return Response('Hello, world!')

if __name__ == "__main__":
    with Configurator() as config:
        # Register a route
        config.add_route('hello', '/')
        # Register view to target by route name
        config.add_view(hello_world, route_name='hello')
        # Creates a WSGI application after all configuration
        app = config.make_wsgi_app()
        # Server configuration
    server = make_server('202.75.56.8', 80, app)
    server.serve_forever()