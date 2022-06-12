from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

# decorator to add an attributes to 'home' function'
# make 'home' function available for scanning later
@view_config(route_name='home', renderer='json')
def home(request):
    return{
        'name': 'Lee Zheng Yang',
        'gender': 'Male'
    }

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route('home', '/')
        # searching configuration declarations in a package and its subpackages
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
