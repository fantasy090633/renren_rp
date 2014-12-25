import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

import sae
import login

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [login.login('18602530273', 'fantasy090633'), login.login('cbcbccbb@126.com', 'chenbin9186')]

application = sae.create_wsgi_app(app)