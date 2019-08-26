import cherrypy

# Run as daemon
from cherrypy.process.plugins import Daemonizer
daemon = Daemonizer(cherrypy.engine,
                    stdout='/root/start_access.log',
                    stderr='/root/start_error.log')
daemon.subscribe()

# Our functions
from file_functions import get_file
from ulmo import *

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return get_file("example.html")

    @cherrypy.expose
    def ulmo(self):
        return ulmotest(self)

    @cherrypy.expose
    def carlos(self):
        return "u nigga, miss u brou, que tal la asiatica?"

    @cherrypy.expose
    def leo(self):
        return "u nigga, miss u brou, que tal las rusas brou?"


def run_server():
    # Set the configuration of the web server
    cherrypy.config.update({
        'engine.autoreload.on': True,
        'log.screen': True,
        'server.socket_port': 80,
        'server.socket_host': '0.0.0.0'
        })

    # Mount the application to CherryPy tree    
    cherrypy.tree.mount(HelloWorld(), '/', config = '/var/www/src/config.cp')

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == "__main__":
    cherrypy.log("main")
    run_server()
