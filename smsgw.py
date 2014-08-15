import random
import string
import os
import subprocess

import cherrypy

class StringGenerator(object):
    cherrypy.config.update({'server.socket_host': '192.168.1.147',
                            'server.socket_port': 8080,
                           })

    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

    @cherrypy.expose
    def sendsms(self, text=unicode(''), phonenumber=''):
        os.system('echo \"{0}\" | gammu sendsms TEXT {1}'.format(text.encode('utf8'), phonenumber))
#        subprocess.call('echo \"{0}\" | gammu sendsms TEXT {1}'.format(text.encode('utf8'), phonenumber))
        return "SMS sent"

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())


